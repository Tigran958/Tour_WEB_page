# Generated by Django 2.2.7 on 2020-03-17 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_tour_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TourImage',
        ),
    ]