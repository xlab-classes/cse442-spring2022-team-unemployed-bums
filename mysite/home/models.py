from django.db import models
from django.utils import timezone
# from django.contrib.auth import User

class Searchtagsmodel(models.Model):
    outdoors = models.BooleanField()
    sports = models.BooleanField()
    recreation = models.BooleanField()
    learning = models.BooleanField()

    def __str__(self):
        return self.title
