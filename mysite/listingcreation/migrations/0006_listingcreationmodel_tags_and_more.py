# Generated by Django 4.0.3 on 2022-05-08 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listingcreation', '0005_remove_listingcreationmodel_recurperiod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingcreationmodel',
            name='tags',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='listingcreationmodel',
            name='eventdate',
            field=models.CharField(default='12/24/2024', max_length=10),
        ),
    ]
