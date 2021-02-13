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
from society_member import views

urlpatterns = [
    path('s_login', views.s_login, name='s_login'),
    path('s_login_evalute',views.s_login_evalute,name='s_login_evalute'),
    path('s_login_cpassword',views.s_login_cpassword,name='s_login_cpassword'),
    path('s_logout', views.s_logout, name='s_logout'),
    path('s_allmember', views.s_allmember, name='s_allmember'),
    path('member_profile/',views.member_profile,name='member_profile'),
    path('member_update_profile/',views.member_update_profile,name='member_update_profile'),
    path('s_notice_view', views.s_notice_view, name='s_notice_view'),
    path('s_gallary', views.s_gallary, name='s_gallary'),
    path('s_v_gallary', views.s_v_gallary, name='s_v_gallary'),
    path('s_visitors_list/',views.s_visitors_list,name='s_visitors_list'),
    path('s_all_contact/',views.s_all_contact,name='s_all_contact'),
    path('s_e_contact/',views.s_e_contact,name='s_e_contact'),
    path('events/',views.events,name='events'),
    path('maintenance/',views.maintenance,name='maintenance'),
    path('complaint/', views.complaint, name='complaint'),
    path('add_complaint/', views.add_complaint, name='add_complaint'),
    path('view_complaint/', views.view_complaint, name='view_complaint'),
]
