# -*- coding: utf-8 -*-
# !/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='wechat-sdk',
    version='0.5.9',
    keywords=('wechat', 'sdk', 'wechat sdk'),
    description=u'微信公众平台Python开发包',
    long_description=open("README.rst").read(),
    license='BSD License',

    url='https://github.com/wechat-python-sdk/wechat-python-sdk',
    author='doraemonext',
    author_email='doraemonext@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    install_requires=map(lambda x: x.replace('==', '>='), open("requirements.txt").readlines()),
)
