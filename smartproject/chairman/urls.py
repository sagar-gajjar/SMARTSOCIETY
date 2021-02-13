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
from chairman import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_evalute/', views.login_evalute, name='login_evalute'),
    path('logout/', views.logout, name='logout'),
    path('chairman_profile/',views.chairman_profile,name='chairman_profile'),
    path('chairman_update_profile/',views.chairman_update_profile,name='chairman_update_profile'),
    path('add_member/',views.add_member,name='add_member'),
    path('register_member/',views.register_member,name='register_member'),
    path('all_members/',views.all_members,name='all_members'),
    path('edit_member_details/<int:pk>',views.edit_member_details,name='edit_member_details'),
    path('update_member_details/',views.update_member_details,name='update_member_details'),
    path('delete_member/<int:pk>',views.delete_member,name='delete_member'),
    path('view_member_details/<int:pk>',views.view_member_details,name='view_member_details'),
    path('view_member/',views.view_member,name='view_member'),
    path('visitors_list/',views.visitors_list,name='visitors_list'),
    path('notice_board/',views.notice_board,name='notice_board'),
    path('notice_sub/',views.notice_sub,name='notice_sub'),
    path('notice_view/',views.notice_view,name='notice_view'),
    path('add_pictures_page/',views.add_pictures_page,name='add_pictures_page'),
    path('add_pictures/',views.add_pictures,name='add_pictures'),
    path('pictures/',views.pictures,name='pictures'),
    path('add_video/',views.add_video,name='add_video'),
    path('upload_video/',views.upload_video,name='upload_video'),
    path('videos/',views.videos,name='videos'),
    path('c_forgot_password/', views.c_forgot_password, name='c_forgot_password'),
    path('e_forgot_password/', views.e_forgot_password, name='e_forgot_password'),
    path('otp_forgot_password/', views.otp_forgot_password, name='otp_forgot_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('delete_picture/<int:pk>', views.delete_picture, name='delete_picture'),
    path('all_contact/',views.all_contact,name='all_contact'),
    path('e_contact/',views.e_contact,name='e_contact'),
    path('add_event_page/', views.add_event_page, name='add_event_page'),
    path('add_event/', views.add_event, name='add_event'),
    path('view_event/', views.view_event, name='view_event'),
    path('edit_event/<int:pk>', views.edit_event, name='edit_event'),
    path('edit_event_detail/', views.edit_event_detail, name='edit_event_detail'),
    path('all_watchman/', views.all_watchman, name='all_watchman'),
    path('watchman_status/<int:pk>/<slug:status>', views.watchman_status, name='watchman_status'),
    path('c_maintenance/', views.c_maintenance, name='c_maintenance'),
    path('add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('view_maintenance/', views.view_maintenance, name='view_maintenance'),
    path('c_view_complaint/', views.c_view_complaint, name='c_view_complaint'),
]
