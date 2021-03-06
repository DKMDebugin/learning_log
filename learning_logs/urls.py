'''Define URL patterns for learning_logs app'''

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),
    # show all topics
    url(r'^topics/$', views.topics, name='topics'),
    # detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Page for adding a new topics
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
