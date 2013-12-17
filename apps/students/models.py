from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User)
    career = models.CharField(max_length=40)

    def __unicode__(self):
        return self.user.username
