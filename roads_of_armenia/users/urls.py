from django.urls import path

from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.home, name='reg_home'),
    path('signup/<int:key>', views.UserSignUpView.as_view(), name='up'),
    path('client_page', views.client_page, name='client_page'),
    path('tour_creation', views.tour_creation, name='tour_creation'),
    path('driver_list', views.driver_list, name='driver_list'),
    path('guide_list', views.guide_list, name='guide_list'),
    path('agent_list', views.agent_list, name='agent_list'),
    path('tour_list', views.tour_list, name='tour_list'),

    path('pic_upload/<int:user_id>/', views.pic_upload, name='pic_upload'),
    path('in/', views.login_0, name='login'),
    path('out/',views.u_logout, name='logout'),

    
]
