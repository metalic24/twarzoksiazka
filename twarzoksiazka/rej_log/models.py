from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, OneToOneField




class User_details(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    profile_img = ImageField(upload_to='profile_pic/', null=True, blank = True)
    bio = models.TextField(blank=True, null=True)
    birth_date = DateField()
    name = CharField(max_length=50, null=False)
    surr_name = CharField(max_length=50, null=False)

    

