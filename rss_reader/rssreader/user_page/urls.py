__author__ = 'naoya-kaige'
from django.conf.urls import patterns, url
from user_page import views

urlpatterns = patterns('',
                       url(r'^$', views.user_page, name='user_page'),
                       url(r'^save/$',views.save_url, name='save_url'),
                       url(r'^feed/$',views.read_feed, name='read_feed'),)