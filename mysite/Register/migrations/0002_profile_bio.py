# Generated by Django 2.0.13 on 2022-04-25 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='stuff'),
            preserve_default=False,
        ),
    ]
