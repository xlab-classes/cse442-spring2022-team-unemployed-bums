# Generated by Django 4.0.3 on 2022-05-02 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listingcreation', '0004_alter_listingcreationmodel_recurperiod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingcreationmodel',
            name='recurperiod',
        ),
        migrations.AlterField(
            model_name='listingcreationmodel',
            name='recurring',
            field=models.CharField(default='No', max_length=20),
        ),
    ]
