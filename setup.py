#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import find_packages, setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


version = '0.2.0.dev0'

setup(
    name='elevation',
    version=version,
    author='Alessandro Amici',
    author_email='alexamici@gmail.com',
    license='Apache License Version 2.0',
    url='https://github.com/bopen/elevation',
    download_url='https://github.com/bopen/elevation/archive/%s.tar.gz' % version,
    description="Global geographic elevation data (CGIAR-CSI SRTM3 V41) for Python.",
    long_description=read('README.rst'),
    packages=find_packages(),
    install_requires=[
        'future',
        'appdirs',
        'rasterio',
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points = {
        'console_scripts': ['eio=elevation.cli:eio'],
    },
)
