from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime
from .choices import *
from multiselectfield import MultiSelectField


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]


class User(AbstractUser):
    username = models.CharField(blank=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    # bank_account = models.CharField(max_length=255)
    # name = models.CharField(max_length=255)
    # phone_number = models.CharField(max_length=30)
    user_choices = models.IntegerField(choices=USER_CHOICES, default=1)
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
    name = models.CharField(max_length=255)
    language = MultiSelectField(_('language'), choices=LANGUAGES_CHOICES)
    about_me = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='img', null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField(choices=AGE_CHOICES)
    experience = models.IntegerField()
    free_days = MultiSelectField(choices=WEEK_DAY_CHOICES)

    car = models.IntegerField(choices=CAR_CHOICES,)
    production_year = models.IntegerField(_('year'), choices=year_choices())
    seats = models.IntegerField()
    kid_seats = models.BooleanField(default=False)
    invalid_chairs = models.BooleanField(default=False)
    price_per_km = models.IntegerField()


class CarImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True)
    image = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='aa')

# class Car(models.Model):
#     car = models.IntegerField(choices=CAR_CHOICES,)
#     production_year = models.IntegerField(_('year'), choices=year_choices())
#     seats = models.IntegerField()
#     kid_seats = models.BooleanField(default=False)
#     invalid_chairs = models.BooleanField(default=False)
#     image = models.ImageField(upload_to='img', null=True)

class Guide(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='guide')
    name = models.CharField(max_length=255)
    language = MultiSelectField(choices=LANGUAGES_CHOICES)
    about_me = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='img', null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField(choices=AGE_CHOICES)
    experience = models.IntegerField()
    tour_type = models.IntegerField(choices=TOUR_CHOICES)
    region = models.IntegerField(choices=REGION_CHOICES)
    free_days = MultiSelectField(choices=WEEK_DAY_CHOICES)
    trip_image = models.ImageField(upload_to='img', null=True, blank=True)
    car_availability = models.BooleanField(default=False)

    car = models.IntegerField(choices=CAR_CHOICES,null=True)
    production_year = models.IntegerField(_('year'), choices=year_choices(), null=True)
    seats = models.IntegerField(null=True)
    kid_seats = models.BooleanField(default=False, null=True)
    invalid_chairs = models.BooleanField(default=False, null=True)
    car_image = models.ImageField(upload_to='img', null=True, blank=True)


    def __str__(self):
        return self.name




class GuideImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True)
    image = models.ForeignKey(Guide, on_delete=models.CASCADE)




class TourAgents(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='touragents') 
    name = models.CharField(max_length=255)   
    # language = models.IntegerField(_('language'), choices=LANGUAGES_CHOICES)
    about_me = models.CharField(max_length=255)
    tour_type = models.IntegerField(_('tour_type'), choices=TOUR_CHOICES)
    # location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tour(models.Model):
    tour = models.ForeignKey(TourAgents, on_delete=models.CASCADE)
    rout = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    date_of_tour = models.DateField(_("Date"), default=datetime.date.today)
    amount_of_place_left = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class TourImage(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True, blank=True)
    image = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name 

class TourAgentImage(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True, blank=True)
    image = models.ForeignKey(TourAgents, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name 