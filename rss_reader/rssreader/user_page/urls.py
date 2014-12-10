__author__ = 'naoya-kaige'
from django.conf.urls import patterns, url
from user_page import views

urlpatterns = patterns('',
                       url(r'^(?P<user_id>\d+)/$', views.user_page, name='user_page'),)