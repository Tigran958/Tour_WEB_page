# Generated by Django 2.2.7 on 2020-03-10 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200310_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touragents',
            name='date_of_tour',
        ),
        migrations.RemoveField(
            model_name='touragents',
            name='first_to_ten_price',
        ),
        migrations.RemoveField(
            model_name='touragents',
            name='quantity',
        ),
    ]
