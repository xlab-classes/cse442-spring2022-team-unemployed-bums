# Generated by Django 2.0.13 on 2022-04-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Searchtagsmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outdoors', models.BooleanField()),
                ('sports', models.BooleanField()),
                ('recreation', models.BooleanField()),
                ('learning', models.BooleanField()),
            ],
        ),
    ]
