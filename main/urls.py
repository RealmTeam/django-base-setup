# -*- coding: utf-8 -*-
from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from main.views import *


urlpatterns = [
    path('', RedirectView.as_view(url=settings.STATIC_URL), name='home'),
    path('api/', include('main.apps.app.urls')),

    path('site-adm/', include('smuggler.urls')),
    path('site-adm/', admin.site.urls),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                                         + static(settings.PROTECTED_URL, document_root=settings.PROTECTED_ROOT)

if not settings.DEBUG:
    urlpatterns.extend([
        # protects the media files from being served if wrong user
        path(r'^{0}<userid>/<filename>'.format(settings.PROTECTED_URL.lstrip('/')), protected_media),
        # protects the media files from being served if not authenticated
        path(r'^{0}<filename>'.format(settings.PROTECTED_URL.lstrip('/')), protected_media)
    ])
