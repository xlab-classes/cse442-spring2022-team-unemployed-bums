# Generated by Django 4.0.3 on 2022-05-02 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listingcreation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingcreationmodel',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listingcreationmodel',
            name='rsvp',
            field=models.IntegerField(default=0),
        ),
    ]