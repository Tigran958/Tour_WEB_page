# Generated by Django 2.2.7 on 2020-04-02 09:34

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_remove_guide_my_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='language',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Armenian'), (2, 'English'), (3, 'France'), (4, 'Russian')], max_length=7, verbose_name='language'),
        ),
    ]
