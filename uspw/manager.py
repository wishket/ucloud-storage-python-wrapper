# -*- coding:utf-8 -*-

import requests
from utils import *
# options is User Account options like Email, Key
try:
    import options
except ImportError:
    pass


class UcloudManager(object):
    host = 'https://api.ucloudbiz.olleh.com'

    def __init__(self, key=None, email=None):
        urls = self.host + '/storage/v1/auth'
        # set request header
        headers = dict()

        if email:
            headers['X-Storage-User'] = email
        else:
            headers['X-Storage-User'] = options.EMAIL

        if key:
            headers['X-Storage-Pass'] = key
        else:
            headers['X-Storage-Pass'] = options.KEY

        response = requests.get(urls, headers=headers)

        # bind authenticated data to instance
        # X-Auth-Token is required all request
        self.auth_token = response.headers['X-Auth-Token']
        self.storage_token = response.headers['X-Storage-Token']
        # X-Storage-Url is authenticated user's target host.
        self.url = response.headers['X-Storage-Url']

        # set base_headers to instance for api
        self.base_headers = dict()
        self.base_headers['X-Auth-Token'] = self.auth_token

    def get_container_of_account(self, limit=None, marker=None,
                                 response_format=None):
        # get authenticated user's container list
        url = self.url
        params = dict()
        if limit:
            params['limit'] = limit
        if marker:
            params['marker'] = marker

        # default format is json
        if not response_format:
            params['format'] = 'json'
            response_format = params['format']
        else:
            params['format'] = response_format

        # request api
        response = requests.get(url, params=params, headers=self.base_headers)

        # formatting result
        result = dict()
        if response_format == 'json' or response_format == 'xml':
            result['container_list'] = response.content
        else:
            result['container_list'] = response.content.split('\n')
            if result['container_list'][-1] == '':
                try:
                    result['container_list'] = result['container_list'][:-2]
                except IndexError:
                    pass

        result['object_count'] = response.headers['X-Account-Object-Count']
        result['used_bytes'] = \
            replace_bytes_to_readable(response.headers['X-Account-Bytes-Used'])
        return result

    def head_account_metadata(self):
        # get account's metadata
        url = self.url

        # request api
        response = requests.head(url, headers=self.base_headers)

        # formatting result
        result = dict()
        result['container_count'] = response.headers['X-Account-Container-Count']
        result['object_count'] = response.headers['X-Account-Object-Count']
        result['used_bytes'] = \
            replace_bytes_to_readable(response.headers['X-Account-Bytes-Used'])
        return result

    def post_account_metadata(self, params, action):
        """
        post account's metadata for add, delete
        :param params: params should iterable by key, value
        :param action: means add or delete ['add', 'delete']
        :return: result status code
        """
        # post account's metadata
        url = self.url

        headers = self.base_headers
        for key, value in params.iteritems():
            if action == 'add':
                headers['X-Account-Meta-' + key] = value
            else:
                headers['X-Remove-Account-Meta-' + key] = value
        response = requests.post(url, headers=headers)
        return response.status_code

    def head_container_metadata(self, container_name):
        # check container metadata
        url = self.url + '/' + container_name

        # request api
        response = requests.head(url, headers=self.base_headers)

        # formatting result
        result = dict()
        result['object_count'] = response.headers['X-Container-Object-Count']
        result['used_bytes'] = \
            replace_bytes_to_readable(response.headers['X-Container-Bytes-Used'])
        return result

    def get_container_objects(self, container_name, limit=None, marker=None,
                              prefix=None, response_format=None, path=None):
        # get object name list in target container
        url = self.url + '/' + container_name

        # make params
        params = dict()
        if limit:
            params['limit'] = limit
        if marker:
            params['marker'] = marker
        if prefix:
            params['prefix'] = prefix

        if not response_format:
            params['format'] = 'json'
            response_format = params['format']
        else:
            params['format'] = response_format

        # TODO: params['path'] should be made

        # request api
        response = requests.get(url, params=params, headers=self.base_headers)

        # formatting result
        result = dict()
        if response_format == 'json' or response_format == 'xml':
            result['object_list'] = response.content
        else:
            result['object_list'] = response.content.split('\n')
            if result['object_list'][-1] == '':
                try:
                    result['object_list'] = result['container_list'][:-2]
                except IndexError:
                    pass

        result['object_count'] = response.headers['X-Container-Object-Count']
        result['used_bytes'] = \
            replace_bytes_to_readable(response.headers['X-Container-Bytes-Used'])

        return result

    def put_container(self, container_name):
        """
        create container for authorized account
        :param container_name: container's name for create
        :return: http response
        """
        # create or update container
        url = self.url + '/' + container_name

        # request api
        response = requests.put(url, headers=self.base_headers)

        return response

    def delete_container(self, container_name):
        """
        delete container for authorized account
        :param container_name: container's name for delete
        :return: http response
        """

        url = self.url + '/' + container_name

        # request api
        response = check_response_status(
            requests.delete(url, headers=self.base_headers)
        )

        return response

    def post_container_metadata(self, container_name, params, action):
        """
        post account's metadata for add, delete
        :param container_name: target container name
        :param params: params should iterable by key, value
        :param action: means add or delete ['add', 'delete']
        :return: result status code
        """
        # post account's metadata
        url = self.url + '/' + container_name

        headers = self.base_headers
        for key, value in params.iteritems():
            if action == 'add':
                headers['X-Container-Meta-' + key] = value
            else:
                headers['X-Remove-Container-Meta-' + key] = value
        response = requests.post(url, headers=headers)
        return response.status_code

    def put_object_to_container(self, container_name,
                              file_path=None,
                              file_name=None,
                              file_stream=None):
        """
        upload file to target container
        :param container_name:
            target container_name - string
            required=True
        :param file_path: file's path for upload - string
        :param file_name: file's name for get urls - string
        :param file_stream: file's data string - string
        :return: submit response
        """

        # make file object to comfortable for uploading
        if not file_name:
            file_name = file_path.split('/')[-1]

        url = self.url + '/' + container_name + '/' + file_name

        if not file_stream:
            file_stream = open(file_path, 'rb').read()

        response = requests.put(
            url,
            data=file_stream,
            headers=self.base_headers
        )

        return response

    def head_object(self, container_name, file_name):
        url = self.url + '/' + container_name + '/' + file_name

        response = check_response_status(
            requests.head(url, headers=self.base_headers)
        )

        return response

    def get_object(self, container_name, file_name, range=None, match=None,
                   none_match=None, modified_since=None, unmodified_since=None):
        url = self.url + '/' + container_name + '/' + file_name

        # TODO: set parameters
        response = check_response_status(
            requests.get(url=url, headers=self.base_headers)
        )

    def post_object_metadata(self, container_name, file_name, params, action):
        """
        post account's metadata for add, delete
        :param params: params should iterable by key, value
        :param action: means add or delete ['add', 'delete']
        :return: result status code
        """
        # post account's metadata
        url = self.url + '/' + container_name + '/' + file_name

        headers = self.base_headers
        for key, value in params.iteritems():
            if action == 'add':
                headers['X-Container-Meta-' + key] = value
            else:
                headers['X-Remove-Container-Meta-' + key] = value
        response = check_response_status(
            requests.post(url, headers=headers)
        )
        return response.status_code

    def copy_object(self, dest_container_name, dest_file_name,
                    target_container_name, target_file_name):

        url = self.url + '/' + dest_container_name + '/' + dest_file_name

        headers = self.base_headers
        headers['X-Copy-From'] = '/' + target_container_name + \
                                 '/' + target_file_name
        headers['Content-Length'] = '0'

        response = check_response_status(
            requests.put(url=url, headers=headers)
        )

        return response

    def delete_object(self, container_name, file_name):
        url = self.url + '/' + container_name + '/' + file_name

        response = check_response_status(
            requests.delete(url=url, headers=self.base_headers)
        )

        return response