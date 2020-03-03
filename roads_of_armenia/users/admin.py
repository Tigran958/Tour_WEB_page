from django.contrib import admin
from .models import *
# register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Driver)
admin.site.register(CarImageModel)
admin.site.register(Guide)
admin.site.register(GuideImageModel)
admin.site.register(TourAgents)
admin.site.register(TourAgentsImageModel)
