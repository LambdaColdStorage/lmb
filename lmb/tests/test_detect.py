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


FEATURES = ['nose', 'eye_left', 'eye_right', 'mouth_left', 'mouth_center',
            'mouth_right']


def face_detected(data, req):
    faces = data.get('images', None)
    # got a face (lenas)
    if len(faces) == 1:
        return True, ''
    else:
        return False, 'Expected non-emty images, got %s' % data


def test_detect_features(img_url='http://lambdal.com/images/test.jpg',
                         features=FEATURES):
    """
    Test 'fast face' feature detection (eyes, nose, mouth filled in)
    """
    def face_detected_with_features(data, req):
        detected, resp = face_detected(data, req)
        if not detected:
            return detected, resp

        images = data.get('images')
        print images
        for img in images:
            for face in img.get('faces', []):
                for feat in features:
                    if not feat in face:
                        print(face)
                        return (False, "Missing a feature from the face: %s"
                                % feat)
        return True, ''

    assert_with(path('/detect?urls=%s' % img_url), face_detected_with_features)


def test_detect(img_url='http://lambdal.com/images/test.jpg'):
    assert_with(path('/detect?urls=%s' % img_url), face_detected)
