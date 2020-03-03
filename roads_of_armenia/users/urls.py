from django.urls import path

from . import views

urlpatterns = [
    path('up', views.StudentSignUpView.as_view()),
]
