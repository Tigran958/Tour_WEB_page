from django.urls import path

from . import views

urlpatterns = [
    path('up/reg_home', views.home, name='reg_home'),
    path('up/<int:key>', views.UserSignUpView.as_view(), name='up'),
]
