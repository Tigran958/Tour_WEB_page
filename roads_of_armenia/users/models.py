from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime

CAR_CHOICES = (
    (1, _("BMW")),
    (2, _("Mercedes Benz"))
)

LANGUAGES_CHOICES = (
    (1, _("Armenian")),
    (2, _("English")),
    (3, _("France")),
    (4, _("Russian")),
)

TOUR_CHOICES = (
    (1, _("Extreme")),
)


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    bank_account = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return "{}".format(self.email)


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='client')
    bonus = models.IntegerField()
    history = models.CharField(max_length=255)


class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='driver')
    car = models.IntegerField(choices=CAR_CHOICES, default=1)
    production_year = models.IntegerField(_('year'), choices=year_choices())
    seats = models.IntegerField()
    price_per_km = models.IntegerField()


class CarImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True)
    image = models.ForeignKey(Driver, on_delete=models.CASCADE)


class Guide(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='guide')
    language = models.IntegerField(_('language'), choices=LANGUAGES_CHOICES)
    about_me = models.CharField(max_length=255)
    first_to_ten_price = models.IntegerField()
    ten_plus_one_price = models.IntegerField()
    location = models.CharField(max_length=255)
    location_based_price = models.IntegerField()


class GuideImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True)
    image = models.ForeignKey(Guide, on_delete=models.CASCADE)


class TourAgents(models.Model):
    language = models.IntegerField(_('language'), choices=LANGUAGES_CHOICES)
    about_me = models.CharField(max_length=255)
    tour_type = models.IntegerField(_('tour_type'), choices=TOUR_CHOICES)


class TourAgentsImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True)
    image = models.ForeignKey(TourAgents, on_delete=models.CASCADE)
