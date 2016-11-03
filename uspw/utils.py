# -*- coding:utf-8 -*-

from exceptions import *


def replace_bytes_to_readable(object_bytes):
    if type(object_bytes) == str:
        object_bytes = float(object_bytes)
    for unit in ['', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']:
        if abs(object_bytes) < 1024.0:
            return "%3.1f%s" % (object_bytes, unit)
        object_bytes /= 1024.0
    return "%.1f%s" % (object_bytes, 'ZB')


def set_django_env(settings):
    if hasattr(settings, 'UCLOUD_EMAIL') and hasattr(settings, 'UCLOUD_KEY'):
        return {'email': settings.UCLOUD_EMAIL,
                'key': settings.UCLOUD_KEY}
    raise ImportError


def check_response_status(response):
    status = response.status_code
    if status == 401:
        raise NotAuthorized
    elif status == 403:
        raise NoPermission
    elif status == 404:
        raise NoContainer
    elif status == 409:
        raise CanNotDelete
    return response


# TODO: json response to python object
