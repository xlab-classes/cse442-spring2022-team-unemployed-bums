from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follow (models.Model):
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

    def __str__(self):
        return "Follow ({} -> {})".format(self.user.username, self.following_user.username)

    class Meta:
        unique_together = ['user', 'following_user']