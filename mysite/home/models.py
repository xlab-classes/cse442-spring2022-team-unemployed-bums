from django.db import models
from django.utils import timezone
# from django.contrib.auth import User

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)