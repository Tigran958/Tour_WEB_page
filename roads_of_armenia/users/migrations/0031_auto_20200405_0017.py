# Generated by Django 2.2.7 on 2020-04-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_touragentimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='first_to_ten_price',
            new_name='amount_of_place_left',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='quantity',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='tour',
            name='name',
            field=models.TextField(),
        ),
    ]