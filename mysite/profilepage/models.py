from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class profiles(models.Model):
    username = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    interests = models.CharField(max_length=200)
    extension = models.CharField(max_length=6)
    imageName = models.CharField(max_length=35)
    imageID = models.IntegerField()
    image = models.ImageField(upload_to='profilepage/images/')
    
    testfield = models.CharField(max_length=200)

class profilePicCounter(models.Model):
    count = 0