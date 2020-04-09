# Generated by Django 2.2.7 on 2020-04-08 21:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20200409_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='language',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', ''), (1, 'Armenian'), (2, 'English'), (3, 'France'), (4, 'Russian')], max_length=8, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='language',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', ''), (1, 'Armenian'), (2, 'English'), (3, 'France'), (4, 'Russian')], default=1, max_length=8),
            preserve_default=False,
        ),
    ]
