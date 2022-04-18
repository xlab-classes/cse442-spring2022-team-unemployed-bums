from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follow (models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following')

    # def __repr__(self):
    #     return "User ({})".format(user.)