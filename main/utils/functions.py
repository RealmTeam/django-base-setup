# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist


def get_one_to_one_or_None(obj, field):
    try:
        return getattr(obj, field, None)
    except ObjectDoesNotExist:
        return None
