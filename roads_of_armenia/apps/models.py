from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import TourAgents, TOUR_CHOICES
# Create your models here.


class Event(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    photo = models.ImageField(upload_to='events')
    description = models.CharField(blank=True, null=True, max_length=255)
    TourAgents = models.OneToOneField(TourAgents,
                                      on_delete=models.CASCADE, related_name='guide')

    def __str__(self):
        return "{}".format(self.name)


class Destination(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    photo = models.ImageField(upload_to='destionations')


class Tour(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    destination = models.ManyToManyField(Destination)
    date = models.DateTimeField()
    description = models.CharField(blank=True, null=True, max_length=255)
    price = models.CharField(blank=True, null=True, max_length=255)
    type = models.IntegerField(_('tour_type'), choices=TOUR_CHOICES)
    amount_of_people = models.IntegerField()
