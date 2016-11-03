# -*- coding:utf-8 -*-

from distutils.core import setup

setup(
    # package name
    name='ucloud-storage-python-wrapper',
    # package version
    version='0.0.7',

    py_modules=['uspw', ],

    # package struct
    packages=['uspw', ],
    license='Apache 2.0',

    author='yonggill Lee',
    author_email='yonggill@wishket.com',
    url='http://blog.yonggari.net',
    description='python wrapper for KT ucloud storage service.',
    keywords=['kt', 'ucloud', 'storage', 'python', 'wrapper']
)