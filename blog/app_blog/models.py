from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
# Create your models here.

class login(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
   
    profile_pic= models.ImageField(upload_to='profile_pics', blank=True)

    def __str__ (self):
        return self.user.username

    # email_id = models.EmailField()
    # password = models.CharField(unique=True, max_length=50)


class blogpage(models.Model):
    # user = models.ForeignKey(name, null=True,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=5000)
    blogs= models.CharField(max_length=50)

