import django_filters
from .models import *


class DriverFilter(django_filters.FilterSet):
	class Meta:
		model = Driver
		fields = ['car','production_year','seats','kid_seats','invalid_chairs',] #must updated#


class TourAgentsFilter(django_filters.FilterSet):
	class Meta:
		model = TourAgents
		fields = '__all__'
		exclude = ('date_of_tour','first_to_ten_price')

class GuideFilter(django_filters.FilterSet):

	class Meta:
		model = Guide
		fields = ['age', 'gender','car_availability',]
		# exclude = ('language','profile_image')

class TourFilter(django_filters.FilterSet):
	class Meta:
		model = Tour
		fields = ["tour",]
		exclude = ('date_of_tour','first_to_ten_price')


