# -*- coding:utf-8 -*-

import requests
# options is User Account options like Email, Key
import options


class UcloudManager(object):
    host = 'https://api.ucloudbiz.olleh.com'

    def __init__(self, key, email):
        urls = self.host + '/storage/v1/auth'
        headers = dict()
        headers['X-Storage-User'] = options.EMAIL
        headers['X-Storage-Pass'] = options.KEY
        response = requests.get(urls, headers=headers)
        self.auth_token = response.headers['X-Auth-Token']
        self.storage_token = response.headers['X-Storage-Token']
        self.url = response.headers['X-Storage-Url']
        self.base_headers = dict()
        self.base_headers['X-Auth-Token'] = self.auth_token

    def get_container_list(self):
        url = self.url
        response = requests.get(url, headers=self.base_headers)
        return response.content.split('\n')

    def head_container_metadata(self, container_name):
        url = self.url + '/' + container_name
        response = requests.head(url, headers=self.base_headers)
        return response.headers

    def get_container_object_list(self, container_name):
        url = self.url + '/' + container_name
        response = requests.get(url, headers=self.base_headers)
        return response

    def put_container(self, container_name):
        url = self.url + '/' + container_name
        response = requests.put(url, headers=self.base_headers)
        return response

    def delete_container(self, container_name):
        url = self.url + '/' + container_name
        response = requests.delete(url, headers=self.base_headers)
        return response

    def put_file_to_container(self, container_name, obj):
        url = self.url + '/' + container_name + '/' + obj.filename
        self.base_headers['Content-Type'] = 'image/png'
        response = requests.put(url, data=open(obj.path, 'rb').read(), headers=self.base_headers)
        return response