""" Defines URL patterns for users app """

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    # Login page
    path(r'login/', LoginView.as_view(template_name= 'users/login.html'), name='login'),
    #Log out url
    path(r'logout/', views.logout_view, name='logout'),
    # Registration Page
    path(r'register/', views.register, name='register'),
]
