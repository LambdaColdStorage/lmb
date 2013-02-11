#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    detect.py
    ~~~~~

    :created: 2013-02-10 22:59:50 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
from core import Img, Rect
from utils import file_url
import cv

def faces_img(img, cascade="haarcascade_frontalface_default.xml"):
    assert instanceof(img, Img), "detect_face requires an img object."
    hc = cv.Load(cascade)
    faces = cv.HaarDetectObjects(img.cv_rep(), hc, cv.CreateMemStorage())
    return [Rect(*rect).dict() for rect,n in faces]

def faces_url(url):
    img = Img(url)
    return faces_img(img)
