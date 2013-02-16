#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    test_detect.py
    ~~~~~~~~~~~~~~

    :created: 2013-02-13 10:03:24 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
from lmb.tests.test_core import assert_with, path


def test_detect(img_url='http://lambdal.com/images/test.jpg'):
    def face_detected(data, req):
        faces = data.get('result', None)
        # got a face (lenas)
        if len(faces) == 1:
            return True, ''
        else:
            return False, 'Expected data, got %s' % data
    assert_with(path('/detect?url=%s' % img_url), face_detected)
