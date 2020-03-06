import django_filters
from .models import *


class DriverFilter(django_filters.FilterSet):
	class Meta:
		model = Driver
		fields = '__all__'

