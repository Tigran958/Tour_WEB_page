# Generated by Django 2.2.7 on 2020-03-11 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_tour_mainimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(blank=True, null=True, upload_to='img')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tour')),
            ],
        ),
    ]
