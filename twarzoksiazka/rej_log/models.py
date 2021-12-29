from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateField, DateTimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField




class User_details(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    profile_img = ImageField(upload_to='profile_pic', default='profile_pic/avatar.jpg',null=True, blank = True)
    bio = models.TextField(blank=True, null=True)
    birth_date = DateField()
    name = CharField(max_length=50, null=False)
    surr_name = CharField(max_length=50, null=False)
    friends = ManyToManyField(User, blank=True, related_name="friends")

    def get_friends(self):
        return self.friends.all()
    def get_friends_no(self):
        return self.friends.all().count()
    def __str__(self):
        return f"{self.user.id}--{self.user.username}"


STATUS_CHOISES ={
    ('send', 'send'),
    ('accepted', 'accepted')
}
    
class Relationship(models.Model):
    sender = ForeignKey(User_details, on_delete=CASCADE, related_name="sender")
    reciver = ForeignKey(User_details, on_delete=CASCADE, related_name="reciver")
    status = CharField(max_length=8, choices=STATUS_CHOISES)
    updated = DateTimeField(auto_now=True)
    created = DateTimeField(auto_now_add=True)