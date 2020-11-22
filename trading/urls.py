from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.signup, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('error/', views.get_error, name='error'),

    path('about/', views.get_about, name='about'),
    path('profile/', views.get_profile, name='profile'),
    path('courses/', views.get_courses, name='courses'),
    path('contact/', views.get_contact, name='contact'),
    path('', views.get_home, name='home'),
]