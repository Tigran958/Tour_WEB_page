import django_filters
from .models import *


class DriverFilter(django_filters.FilterSet):
	class Meta:
		model = Driver
		fields = '__all__'

class TourAgentsFilter(django_filters.FilterSet):
	class Meta:
		model = TourAgents
		fields = '__all__'
		exclude = ('date_of_tour','first_to_ten_price')

class GuideFilter(django_filters.FilterSet):
	class Meta:
		model = Guide
		fields = '__all__'

