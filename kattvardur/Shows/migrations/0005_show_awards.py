# Generated by Django 3.2.8 on 2021-10-09 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Awards', '0001_initial'),
        ('Shows', '0004_auto_20211009_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='awards',
            field=models.ManyToManyField(to='Awards.Award'),
        ),
    ]
