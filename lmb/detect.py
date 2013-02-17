#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    detect.py
    ~~~~~

    :created: 2013-02-10 22:59:50 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
from core import Img, Rect, Face
from utils import cascade_path
import cv


def faces_img(img, cascade="haarcascade_frontalface_default.xml", min_n=5):
    assert isinstance(img, Img), "detect_face requires an img object."
    hc = cv.Load(cascade_path(cascade))
    faces = cv.HaarDetectObjects(img.cv_rep(), hc, cv.CreateMemStorage())
    return [Face(Rect(*rect), n, img).dict() for rect, n in faces if n > min_n]


def img_url(url, detect=True):
    if not url:
        return []
    img = Img(url)
    img.faces = faces_img(img)
    return img
