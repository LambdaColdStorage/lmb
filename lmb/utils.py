#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    utils.py
    ~~~~~

    :created: 2013-02-10 23:16:24 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
from contextlib import closing
import urllib2
import cStringIO
from urlparse import urlparse
from PIL import Image as PILImage
import os


cwd = os.path.dirname(__file__)


class LambdaExcept(Exception):
    pass


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
    pi = PILImage.open(file_url(path))
    return pi


def cascade_path(path):
    path = os.path.join(cwd, 'cascades/', path)
    return path
