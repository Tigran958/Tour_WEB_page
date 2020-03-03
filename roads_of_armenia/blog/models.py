from django.db import models

# Create your models here.


class Post(models.Model):
    topic = models.CharField(blank=True, null=True, max_length=30)
    images = models.ImageField(upload_to='events')
    description = models.CharField(blank=True, null=True, max_length=255)
