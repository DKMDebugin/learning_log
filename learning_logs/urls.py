'''Define URL patterns for learning_logs app'''

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),
]
