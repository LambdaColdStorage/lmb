#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    utils.py
    ~~~~~

    :created: 2013-02-10 23:16:24 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
import os
import datetime
from contextlib import closing
import urllib2
import cStringIO
from urlparse import urlparse
from PIL import Image as PILImage
import collections


module_name = 'lmb'
cwd = os.path.dirname(__file__)


class LambdaExcept(Exception):
    pass


def tuple_rect(rect):
    return rect['x'], rect['y'], rect['w'], rect['h']


def is_rect(rect):
    if not isinstance(rect, collections.Iterable):
        return False
    rect_keys = ['x', 'y', 'w', 'h']
    return all(k in rect for k in rect_keys)


def file_url(url):
    """url -> file
    """
    try:
        with closing(urllib2.urlopen(url)) as u:
            f = cStringIO.StringIO(u.read())
    except urllib2.URLError:
        raise LambdaExcept("Got an error when opening the url. The network \
                connection might be down.")
    return f


def file_fpath(fpath):
    return open(fpath)


def file_path(path):
    """path(url || filepath) -> file
    """
    parsed = urlparse(path)
    if 'http' in parsed.scheme:
        return file_url(path)
    else:
        return open(path)


def pil_path(path):
    """Make a PIL Image given a URL/fname
    """
    pi = PILImage.open(file_path(path))
    return pi


def cascade_path(path):
    path = os.path.join(cwd, 'cascades/', path)
    return path


def fname(filepath):
    head, tail = os.path.split(filepath)
    return tail


def pretty_date(date):
    return date.strftime('%Y-%m-%d')


def pretty_now():
    return pretty_date(datetime.datetime.now())


def new_name(src, prefix='draw'):
    """path, prefix -> new path with prefix
    """
    head, tail = os.path.split(src)
    pwd = os.getcwd()
    return os.path.join(pwd, ('%s_' % prefix) + tail)
