from django.urls import path

from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('up/reg_home', views.home, name='reg_home'),
    path('up/<int:key>', views.UserSignUpView.as_view(), name='up'),
    path('up/client_page', views.client_page, name='client_page'),
    path('up/driver_list', views.driver_list, name='driver_list'),
    path('up/guide_list', views.guide_list, name='guide_list'),
    path('up/agent_list', views.agent_list, name='agent_list'),


    path('in/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/profile/',views.login_1, name='login_1'),
    path('out/',views.u_logout, name='logout'),

    
]
