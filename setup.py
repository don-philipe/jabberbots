#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='jabberbots',
    version='0.0.1',
    description='A set of bots for jabber/xmpp',
    packages=find_packages(include=['src.*']),
    python_requires='>=3.8',
    install_requires=[
        'aioopenssl==0.5.1',
        'aiosasl==0.4.1',
        'aioxmpp==0.13.1',
        'Babel==2.9.0',
        'cffi==1.14.4',
        'cryptography==3.3.1',
        'dnspython==1.15.0',
        'dnspython3==1.15.0',
        'lxml==4.7.1',
        'multidict==4.7.6',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pycparser==2.20',
        'pyOpenSSL==20.0.1',
        'pytz==2020.5',
        'six==1.15.0',
        'sortedcollections==1.2.3',
        'sortedcontainers==2.3.0',
        'tzlocal==1.5.1',
    ],
    package_data={
        'config': ['config.example.json'],
    },
    entry_points={
        'console_scripts': [
            'start=jabberbots:main',
        ],
    },
)
