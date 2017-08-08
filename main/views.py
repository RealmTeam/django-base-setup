# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.conf import settings


@login_required
def protected_media(request, userid="", filename=""):
    response = HttpResponse()
    if userid:
        if request.user.is_superuser or userid == request.user.id:
            response['X-Accel-Redirect'] = settings.PROTECTED_URL + "/".join(userid, filename)
        else:
            raise Http404
    else:
        response['X-Accel-Redirect'] = settings.PROTECTED_URL + filename
    return response
