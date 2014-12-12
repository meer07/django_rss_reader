from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('user_manager.urls', namespace='user_manager')),
    url(r'^user/', include('user_page.urls', namespace='user_page')),
)
