# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from main.views import *


urlpatterns = [
    url(r'^$', RedirectView.as_view(url=settings.STATIC_URL), name='home'),
    url(r'^api/', include('main.apps.app.urls')),

    url(r'^site-adm/', include('smuggler.urls')),
    url(r'^site-adm/', include(admin.site.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                                         + static(settings.PROTECTED_URL, document_root=settings.PROTECTED_ROOT)

if not settings.DEBUG:
    urlpatterns.extend([
        # protects the media files from being served if wrong user
        url(r'^{0}(?P<userid>[^/]+)/(?P<filename>[^/]+)$'.format(settings.PROTECTED_URL.lstrip('/')), protected_media),
        # protects the media files from being served if not authenticated
        url(r'^{0}(?P<filename>[^/]+)$'.format(settings.PROTECTED_URL.lstrip('/')), protected_media)
    ])
