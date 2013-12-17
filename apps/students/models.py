from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()

    def __unicode__(self):
        return self.user.username
