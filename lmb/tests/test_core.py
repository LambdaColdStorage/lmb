#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
        test_core.py
        ~~~~~

        :copyright: (c) by Lambda Labs, Inc.
        :license: BSD. See LICENSE.
"""
from lmb.tests import DEFAULT_PORT

def code_is(code=200, resp=None):
    got = rep.code
    assert got == code, 'HTTP code expected: %d, got %d' % (code, got)

def successful_response(pydata, resp):
    assert resp.code == 200, 'HTTP code not 200, got %d' % resp.code
    return 'status' in pydata

def test_server(url="http://localhost:%s" % DEFAULT_PORT):
    with urllib.urlopen(url) as u:
        pydata = json.loads(u.read())
        assert successful_response(pydata, u), \
            'Response should be json deserializable, got: %s' % pydata
