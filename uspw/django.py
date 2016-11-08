# -*- coding:utf-8 -*-

from uspw.manager import UcloudManager
from uspw.exceptions import NoTargetObject, ImportDjangoError

try:
    from django.conf import settings
    from django.core.files.storage import Storage
except ImportError:
    raise ImportDjangoError

# for django filesystem.
# models.FileField(storage=UcloudStorage)
# set configuration for default container


class UcloudStorage(Storage):
    def __init__(self, target_container=None):
        if target_container:
            self.manager = UcloudManager()
            self.container_name = target_container
        elif hasattr(settings, 'UCLOUD_CONTAINER_NAME'):
            self.manager = UcloudManager()
            self.container_name = settings.UCLOUD_CONTAINER_NAME
        else:
            raise

    def exists(self, name):
        return self.manager.head_object(
            self.container_name, name
        )

    def delete(self, name):
        try:
            self.manager.delete_object(self.container_name, name)
        except NoTargetObject:
            pass

    def size(self, name):
        return self.manager.head_object(
            self.container_name, name
        )['Content-Length']

    def open(self, name, mode='rb'):
        return self.manager.get_object(self.container_name, name)

    def listdir(self, path):
        pass

    def url(self, name):
        return '/media/' + name

    def save(self, name, content, max_length=None):
        self.manager.put_object_to_container(
            self.container_name,
            file_name=name,
            file_stream=content
        )

        return name
