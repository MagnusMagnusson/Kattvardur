# Generated by Django 3.2.8 on 2021-10-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='litter',
            name='entries',
            field=models.ManyToManyField(to='Shows.Entry'),
        ),
    ]
