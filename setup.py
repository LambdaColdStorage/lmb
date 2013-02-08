# -*- coding: utf-8 -*-
"""
Lambda
========

Lambda is a toolkit for image processing and pattern recognition.

Information and examples can be found on the `Lambda Labs homepage <http://lambdal.com/>`_.

Features
--------

Contribute
-------------------

Fork us on `github`_::

    git clone git@github.com:lambdal/lambda.git

.. _github: http://github.com/lambdal/lambda
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='Lambda',
    version='0.1-dev',
    url='http://lambdal.com',
    license='MIT',
    author='Stephen A. Balaban',
    author_email='s@lambdal.com',
    description='Computer vision, without the Ph.D.',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    packages=['lambda'],
    include_package_data=True,
    platforms='any'
)
