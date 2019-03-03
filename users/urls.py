""" Defines URL patterns for users app """

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Login page
    url(r'^login/$', LoginView, {'template_name': 'users/login.html'}, name='login'),
]
