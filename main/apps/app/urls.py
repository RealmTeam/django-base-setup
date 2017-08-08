# -*- coding: utf-8 -*-

"""This module links each view to an url and give it a name"""

from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
# router.register(r'my', MyViewSet)


urlpatterns = router.urls + []
