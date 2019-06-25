from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class LostPeople(models.Model):
    user            = models.ForeignKey(User, related_name='user_with_lost_person', null=True, blank=True)
    photo           = models.CharField(max_length=20)
    name            = models.CharField(max_length=20)

    def __str__(self):
        return self.user.email
    def __unicode__(self):
        return self.user.email

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3442524535)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "img/{new_filename}/{final_filename}".format(
            new_filename = new_filename,
            final_filename = final_filename
            )

class FindPeople(models.Model):
    user = models.ForeignKey(User, related_name='user_finding_the_person', null=True, blank=True)
    lost_person = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
