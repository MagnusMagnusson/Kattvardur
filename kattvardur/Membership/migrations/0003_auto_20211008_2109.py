# Generated by Django 3.2.8 on 2021-10-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Membership', '0002_auto_20211008_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='uri',
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.CharField(max_length=7, primary_key=True, serialize=False, unique=True),
        ),
    ]
