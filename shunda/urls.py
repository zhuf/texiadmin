from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from texi.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shunda.views.home', name='home'),
    # url(r'^shunda/', include('shunda.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^accounts/login/$', login_view),
    url(r'^accounts/logout/$', logout_view),
    url(r'^accounts/profile/$', profile_view), 
    url(r'^display/$', display_meta),
    url(r'^office/notification/$', notificationedit),
    url(r'^$', index),
    url(r'^test', test),


    url(r'^driver/list/(\w+)', driver_list),
    url(r'^driver/single/(\d+)', driver_single),
    url(r'^driver/edit/(\d+)', driver_edit),
    url(r'^driver/add', driver_add),
    url(r'^deletedriver/(\d+)', deletedriver),
 


    url(r'^car/list/', car_list),
    url(r'^car/single/(\d+)', car_single),
    url(r'^car/edit/(\d+)', car_edit),
    url(r'^car/add', car_add),
    url(r'^deletecar/(\d+)', deletecar),    
    url(r'^delcardriver/(\d+)/(\d+)', del_car_driver),



)
