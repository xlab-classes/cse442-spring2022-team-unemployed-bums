from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Follow (models.Model):
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

    def __str__(self):
        return "Follow ({} -> {})".format(self.user.username, self.following_user.username)

    class Meta:
        unique_together = ['user', 'following_user']

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

	def __str__(self):
		return '{} Profile'.format(self.user.username)
	
	def save(self, *args, **kwargs):
		super().save() 
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


	