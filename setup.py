#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


__about__ = {}
with io.open(join(dirname(__file__), "src", "hybtools", "__about__.py")) as fp:
    exec(fp.read(), __about__)


with io.open(join(dirname(__file__), 'README.rst'), encoding='utf-8') as fp:
    __long_description__ = fp.read()


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name=__about__['__name__'],
    version=__about__['__version__'],
    license=__about__['__license__'],
    description=__about__['__description__'],
    long_description=__long_description__,
    author=__about__['__author__'],
    author_email=__about__['__email__'],
    url=__about__['__url__'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Biologists',
        'License :: OSI Approved :: GPL License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    keywords='bioinformatics CLASH hybrids',
    install_requires=[
        'aenum',
        'click',
        'pandas'
    ],
    extras_require={'test': ['pytest', 'tox']},
    entry_points={
        'console_scripts': [
            'hybtools = hybtools.cli:main',
        ]
    },
)
