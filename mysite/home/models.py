from django.db import models

class Searchtagsmodel(models.Model):
    outdoors = models.BooleanField()
    sports = models.BooleanField()
    recreation = models.BooleanField()
    learning = models.BooleanField()

    def __str__(self):
        return self.title