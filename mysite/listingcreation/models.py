from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

search_tag_choices = ['Outdoors', 'sports', 'recreational', 'edjucational']
daychoices = [('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20'),('21', '21'),('22', '22'),('23', '23'),('24', '24'),('25', '25'),('26', '26'),('27', '27'),('28', '28'),('29', '29'),('30', '30'),('31', '31')]
monthchoices = [('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12')]
yearchoices = [('2022', '2022'),('2023', '2023'),('2024', '2024')]

class ListingCreationModel(models.Model):
    title = models.CharField(max_length=200)
    #author = models.CharField(max_length=200, default="anonymous")
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, default="anonymous")
    created_on = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    eventdate = models.CharField(max_length=10, default="4/11/2022")
    outdoors = models.BooleanField()
    sports = models.BooleanField()
    recreation = models.BooleanField()
    learning = models.BooleanField()
    learning = models.BooleanField()
    hidden = models.BooleanField(default=False)
    rsvp = models.IntegerField(default=0)

    def __str__(self):
        return self.title