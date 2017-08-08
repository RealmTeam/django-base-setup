# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners of an object to view and edit it.
    Assumes the model instance has a `has_access` function returning a list of User model.
    """

    def has_object_permission(self, request, view, obj):
        try:
            return request.user in obj.has_access()
        except AttributeError:
            return False
