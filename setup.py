# -*- coding: utf-8 -*-
"""
lmb
========

lmb is a toolkit for image processing and pattern recognition.

Information and examples can be found on the `Lambda Labs homepage
<http://lambdal.com/>`_.

Features
--------

Contribute
-------------------

Fork us on `github`_::

    git clone git@github.com:lambdal/lmb.git

.. _github: http://github.com/lambdal/lmb
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='lmb',
    version='0.1-dev',
    url='http://lambdal.com',
    license='BSD',
    author='Stephen A. Balaban',
    author_email='s@lambdal.com',
    description='Computer vision, without the Ph.D.',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    packages=['lmb'],
    include_package_data=True,
    platforms='any'
)
