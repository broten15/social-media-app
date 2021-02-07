"""Defines URL patterns for users"""

from django.conf.urls import url
from django.urls import re_path
from django.contrib.auth.views import LoginView
from django.urls.conf import path

from . import views

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # Logout page
    path('logout/', views.logout_view, name='logout'),

    # Registration page
    path('register/', views.register, name='register'),

    # User profile
    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),

]

