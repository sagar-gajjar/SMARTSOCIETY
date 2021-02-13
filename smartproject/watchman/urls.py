"""smartproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from watchman import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('register_watchman/', views.register_watchman, name='register_watchman'),
    path('w_login/', views.w_login, name='w_login'),
    path('w_index/', views.w_index, name='w_index'),
    path('w_login_evalute/', views.w_login_evalute, name='w_login_evalute'),
    path('w_logout/', views.w_logout, name='w_logout'),
    path('watchman_profile/', views.watchman_profile, name='watchman_profile'),
    path('watchman_update_profile/', views.watchman_update_profile, name='watchman_update_profile'),
    path('w_allmember/', views.w_allmember, name='w_allmember'),
    path('w_view_member/<int:pk>', views.w_view_member, name='w_view_member'),
    path('w_notice_view', views.w_notice_view, name='w_notice_view'),
    path('w_gallary', views.w_gallary, name='w_gallary'),
    path('w_v_gallary', views.w_v_gallary, name='w_v_gallary'),
    path('w_all_contact/',views.w_all_contact,name='w_all_contact'),
    path('w_e_contact/',views.w_e_contact,name='w_e_contact'),
    path('w_events/',views.w_events,name='w_events'),
    path('w_visitors/', views.w_visitors, name='w_visitors'),
    path('w_add_visitors/', views.w_add_visitors, name='w_add_visitors'),
    path('w_visitors_list/',views.w_visitors_list,name='w_visitors_list'),
]