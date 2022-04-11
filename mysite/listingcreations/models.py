from django.db import models
import uuid

search_tag_choices = ['Outdoors', 'sports', 'recreational', 'edjucational']

class ListingCreationModel(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    outdoors = models.BooleanField()
    sports = models.BooleanField()
    recreation = models.BooleanField()
    learning = models.BooleanField()

    def __str__(self):
        return self.title