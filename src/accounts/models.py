from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)
import random
import os

from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

class UserManager(BaseUserManager):
# If full_name is a required field you will have to pass in this method
    def create_user(self, email, mobile_no, full_name, password=None, is_active=True, is_admin=False, is_staff=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not mobile_no:
            raise ValueError("Users must have a mobile number")
        if not full_name:
            raise ValueError("Users must have a full name")

        user_obj = self.model(
            email = self.normalize_email(email),
            mobile_no = mobile_no,
            full_name = full_name,
        )
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, mobile_no, full_name, password=None):
        user = self.create_user(
            email,
            mobile_no,
            full_name,
            password = password,
            is_staff = True,
        )
        return user

    def create_superuser(self, email, mobile_no=None, full_name=None, password=None):
        user = self.create_user(
            email,
            mobile_no,
            full_name,
            password = password,
            is_staff = True,
            is_admin = True,
        )
        return user

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3442524535)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "users/{new_filename}/{final_filename}".format(
            new_filename = new_filename,
            final_filename = final_filename
            )

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    mobile_no = models.DecimalField(decimal_places=0, max_digits=20, null=True)
    full_name = models.CharField(max_length=255, null=True)
    profile_photo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    latitude = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    staff = models.BooleanField(default=False) # staff user ( non super user )
    active = models.BooleanField(default=True) # can login
    admin = models.BooleanField(default=False) # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)
    ngo = models.BooleanField(default=False)
    objects = UserManager()
    # confirm = models.BooleanField(defualt=False)
    # confirm_date = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    # email and password are required by default
    REQUIRED_FIELDS = ['mobile_no','full_name'] # ['full_name'] --> python manage.py createsuperuser will ask for required fields in list

    def __str__(self):
        return self.email

    def get_mobile_no(self):
        return self.mobile_no

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.full_name

# These below two methods are by default methods to be overidden acc to documentatiob
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

def user_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(user_pre_save_reciever, sender = User)
