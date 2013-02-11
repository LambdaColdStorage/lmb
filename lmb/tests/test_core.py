#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
        test_core.py
        ~~~~~

        :copyright: (c) by Lambda Labs, Inc.
        :license: BSD. See LICENSE.
"""
from contextlib import closing
from lmb import DEFAULT_PORT
import json
import urllib2
import urlparse

SERVER="http://localhost:%s" % DEFAULT_PORT

def path(p, base=SERVER):
    return urlparse.urljoin(base, p)

def assert_with(url, pred):
    """
    Assert predicate function.
    
    Predicate function takes pydata, request obj -> returns result, string
    """
    with closing(urllib2.urlopen(url)) as r:
        pydata = json.loads(r.read())
        pred, strn = pred(pydata, r)
        assert pred, strn


def code_is(code=200, resp=None):
    got = rep.code
    assert got == code, 'HTTP code expected: %d, got %d' % (code, got)

def successful_response(pydata, resp):
    assert resp.code == 200, 'HTTP code not 200, got %d' % resp.code
    return 'status' in pydata

def server_online(url):
    try:
        urllib2.urlopen(url)
        return True
    except urllib2.URLError:
        return False
    return False

def test_server(url=SERVER):
    assert server_online(url), "Expected to see the server online at %s." % url
    with closing(urllib2.urlopen(url)) as u:
        pydata = json.loads(u.read())
        assert successful_response(pydata, u), \
            'Response should be json deserializable, got: %s' % pydata

def test_detect(img_url='http://lambdal.com/images/test.jpg'):
    def face_detected(data, req):
        faces = data.get('result', None)
        if len(faces) == 1: # got a face (lenas)
            return True, ''
        else:
            return False, 'Expected data, got %s' % data
    assert_with(path('/detect?url=%s' % img_url), face_detected)
