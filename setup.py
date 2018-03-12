#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='hybtools',
    version='0.0.1',
    license='GPL license',
    description='Hybtools description.',
    long_description='A suite of command line tools for working with hyb and viennad files.',
    author='Hywel Dunn-Davies',
    author_email='hyweldunndavies@gmail.com',
    url='https://github.com/hyweldunndavies/hybtools',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Biologists',
        'License :: OSI Approved :: GPL License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    keywords=[],
    install_requires=[
        'pytest',
        'click',
        'pandas'
    ],
    extras_require={},
    entry_points={
        'console_scripts': [
            'hybtools = hybtools.cli:main',
        ]
    },
)
