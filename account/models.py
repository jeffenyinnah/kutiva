from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

#
# class Perfil(models.Model):
#     user = models.ForeignKey(User, on_delete="CASCADE", blank=True)
