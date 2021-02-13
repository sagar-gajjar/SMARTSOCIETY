"""epolicestation URL Configuration

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
from citizen import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register_page/', views.register_page, name='register_page'),
    path('register_member/', views.register_member, name='register_member'),
    path('login_evaluate/', views.login_evaluate, name='login_evaluate'),
    path('logout/', views.logout, name='logout'),
    path('law_details/',views.law_details, name='law_details'),
    path('citizen_dashboard/',views.citizen_dashboard,name='citizen_dashboard'),
    path('citizen_profile/', views.citizen_profile, name='citizen_profile'),
    path('add_fir/', views.add_fir, name='add_fir'),
    path('add_complaint/',views.add_complaint, name='add_complaint'),
    path('submit_complaint/',views.submit_complaint, name='submit_complaint'),
    path('verify_otp/',views.verify_otp, name='verify_otp'),
    path('forgot_password/',views.forgot_password, name='forgot_password'),
    path('enter_new_password/',views.enter_new_password,name='enter_new_password'),
]

   
