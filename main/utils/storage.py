# -*- coding: utf-8 -*-

from django.core.files.storage import FileSystemStorage
from django.conf import settings


protected_media = FileSystemStorage(location=settings.PROTECTED_ROOT,
                                    base_url=settings.PROTECTED_URL)
