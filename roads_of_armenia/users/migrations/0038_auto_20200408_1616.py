# Generated by Django 2.2.7 on 2020-04-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20200407_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='image',
        ),
        migrations.AddField(
            model_name='guide',
            name='car_image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
