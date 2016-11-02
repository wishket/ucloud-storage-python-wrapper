# -*- coding:utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    # package name
    name='ucloud-python-wrapper',
    # package version
    version='0.0.1',

    # package struct
    packages=['uspw', ],
    package_dir={'uspw': 'ucloud-storage-python-wrapper'},
    license='Apache 2.0',

    author='yonggill Lee',
    author_email='yonggill@wishket.com',
    url='http://blog.yonggari.net',
    description='python wrapper for KT ucloud storage service.'
)