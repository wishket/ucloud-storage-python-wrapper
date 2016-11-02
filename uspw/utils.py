# -*- coding:utf-8 -*-


def replace_bytes_to_readable(object_bytes):
    if type(object_bytes) == str:
        object_bytes = float(object_bytes)
    for unit in ['', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']:
        if abs(object_bytes) < 1024.0:
            return "%3.1f%s" % (object_bytes, unit)
        object_bytes /= 1024.0
    return "%.1f%s" % (object_bytes, 'ZB')
