# Generated by Django 2.2.7 on 2020-03-09 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200309_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='touragents',
            name='first_to_ten_price',
            field=models.IntegerField(default=0),
        ),
    ]
