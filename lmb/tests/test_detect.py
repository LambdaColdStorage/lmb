#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    test_detect.py
    ~~~~~

    :created: 2013-02-15 22:21:57 -0800
    :copyright: (c) 2013, Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
from test_core import assert_with, path


def face_detected(data, req):
    faces = data.get('result', None)
    # got a face (lenas)
    if len(faces) == 1:
        return True, ''
    else:
        return False, 'Expected data, got %s' % data


def face_detected_with_features(data, req):
    """
    asserts that a face has features like eyes, nose, mouth
    """
    fd, st = face_detected(data, req)
    # no faces detected? return
    if not fd:
        return fd, st
    faces = data.get('result', None)
    return all([face.get('eye_left', None) for face in faces]), ''
        


def test_detect(img_url='http://lambdal.com/images/test.jpg'):
    assert_with(path('/detect?url=%s' % img_url), face_detected)
