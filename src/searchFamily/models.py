from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
User = get_user_model()

class Family(models.Model):
    user            = models.ForeignKey(User, related_name='user', null=True, blank=True)
    family_members  = models.ForeignKey(User, related_name='family_members',blank=True)
    relationship    = models.TextField()
    status          = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    def __unicode__(self):
        return self.user.email

    def get_absolute_url(self):
        # return "/family/{slug}/".format(slug=self.family_members.slug)
        return reverse("user:details", kwargs={"slug": self.family_members.slug})
