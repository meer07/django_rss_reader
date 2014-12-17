__author__ = 'naoya-kaige'
from django.conf.urls import patterns, url
from user_manager import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^create_user/$', views.create_user, name='create_user'),
                       url(r'^login/$', views.login, name='login'),
                       url(r'^logout/$', views.logout, name='logout'),)