# -*- coding:utf-8 -*-

import requests

class UcloudManager(object):
    def __init__(self, key):
        urls = 'https://api.ucloudbiz.olleh.com/storage/v1/auth'
        headers = dict()
        headers['X-Storage-User'] = 'admin@wishket.com'
        headers['X-Storage-Pass']
        requests.get(urls)