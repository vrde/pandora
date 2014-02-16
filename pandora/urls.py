from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pandora.views.home', name='home'),
    url(r'ajax-upload$', 'pandora.views.import_uploader', name='ajax-upload'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
        (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.UPLOAD_PATH}),
    )
