from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class profiles(models.Model):
    username = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    interests = models.CharField(max_length=200)
   

    image = models.ImageField(upload_to='images/')
    
    testfield = models.CharField(max_length=200)

class profileImage(models.Model):
    name = models.CharField(max_length=50)
    imageFile = models.ImageField(upload_to='profilepage/djangoImages/')
    #extension = models.CharField(max_length=6)
    #imageName = models.CharField(max_length=35)
    #imageID = models.IntegerField()


class profilePicCounter(models.Model):
    count = 0