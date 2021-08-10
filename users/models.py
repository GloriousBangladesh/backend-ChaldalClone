from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=20, default=None, blank=True, null=True)
    cart = models.JSONField(default=dict, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']