#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    test_detect.py
    ~~~~~~~~~~~~~~

    :created: 2013-02-13 10:03:24 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
from functools import partial
from lmb.tests.test_core import assert_with, path


FEATURES = ['nose', 'eye_left', 'eye_right', 'mouth_left', 'mouth_center',
            'mouth_right']

# test URLs for gender classifier
GENDER_TEST = {'female': ['http://lambdal.com/images/test.jpg',
                          'http://lambdal.com/images/test2.jpg'],
               'male': []}
TEST_URLS = GENDER_TEST['female']


def face_detected_with_features(data, req, features=FEATURES):
    detected, resp = face_detected(data, req, 1)
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


def face_detected_with_gender(data, req, gender):
    assert gender in GENDER_TEST.keys(), "Must provide a gender!"
    detected, resp = face_detected(data, req, 1)
    if not detected:
        return False, resp

    images = data.get('images')
    for img in images:
        for face in img.get('faces', []):
            detected_gender = face.get('gender', None)
            if not detected_gender:
                return False, "Didn't find a gender on the face."
            if detected_gender == gender:
                return True, ''
            else:
                return False, 'Expected gender %s, got %s' % (gender,
                              detected_gender)
    return False, 'Got empty images or no detections.'


def test_gender(img_urls=TEST_URLS):
    """Assert that all female faces have been classified as such!
    """
    assert_with(path('/detect?urls=%s' % ','.join(img_urls)),
                partial(face_detected_with_gender, gender='female'))


def face_detected(data, req, count=1):
    images = data.get('images', [])
    if not images:
        return False, 'Expected to find images in data, got %s' % data
    for img in images:
        faces = img.get('faces', [])
        # got a face (lenas)
        if len(faces) == count:
            return True, ''
        else:
            return False, 'Expected only %d face(s), got %d' % (count,
                                                                len(faces))


def test_detect_features(img_url=TEST_URLS[0], features=FEATURES):
    """Test 'fast face' feature detection (eyes, nose, mouth filled in)
    """
    assert_with(path('/detect?urls=%s' % img_url),
                partial(face_detected_with_features, features=features))


def test_detect_single_face(img_url='http://lambdal.com/test2.jpg'):
    """Assert that there's only one face detected in this image
    """
    assert_with(path('/detect?urls=%s' % img_url), partial(face_detected,
                count=1))


def test_detect(img_url=TEST_URLS[0]):
    assert_with(path('/detect?urls=%s' % img_url), face_detected)
