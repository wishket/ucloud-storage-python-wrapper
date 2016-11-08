# -*- coding:utf-8 -*-

from distutils.core import setup

setup(
    # package name
    name='ucloud-storage-python-wrapper',
    # package version
    version='0.1.1',

    py_modules=['uspw', ],

    # package struct
    packages=['uspw', ],
    license='GNU GPL 3.0',

    author='yonggill Lee',
    author_email='yonggill@wishket.com',
    url='https://www.wishket.com',
    description='python wrapper for KT ucloud storage service.',
    keywords=['kt', 'ucloud', 'storage', 'python', 'wrapper']
)