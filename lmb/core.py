#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    core.py
    ~~~~~

    Core classes of Lambda Labs

    :created: 2013-02-10 23:26:11 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
import cv
from utils import pil_path


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dict(self):
        return {
            'x': self.x,
            'y': self.y
        }


class Size(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def dict(self):
        return {
            'w': self.w,
            'h': self.h
        }


class Rect(object):
    """Rectangle object

    :param x: x coord
    :param y: y coord
    :param w: width
    :param h: height
    """
    def __init__(self, x, y, w, h):
        self.point = Point(x, y)
        self.size = Size(w, h)

    @property
    def x(self):
        return self.point.x

    @property
    def y(self):
        return self.point.y

    @property
    def w(self):
        return self.size.w

    @property
    def h(self):
        return self.size.h

    def __repr__(self):
        return self.dict()

    def dict(self):
        return dict(x=self.x, y=self.y, w=self.w, h=self.h)


class Img(object):
    """Core lambda labs image object

    :param src: url/file of an image
    """
    def __init__(self, src):
        self.src = src
        self.img_pil = pil_path(src)
        self.faces = []

    def cv_rep(self):
        """OpenCV representation of this image.
        """
        pc = self.img_pil.convert('L')
        cvi = cv.CreateImageHeader(pc.size, cv.IPL_DEPTH_8U, 1)
        cv.SetData(cvi, pc.tostring(), pc.size[0])
        self.img_cv = cvi
        return cvi

    def dict(self):
        d = {
            'source': self.src,
        }
        if self.faces:
            d['faces'] = self.faces
        return d


class Face(object):
    """Core face object

    :param rect: rectangle around face
    :param n: neighbors from detection
    :param img: source img reference of the detected face
    """
    def __init__(self, rect, n, img):
        self.rect = rect
        self.n = n
        self.img = img

    @property
    def features(self):
        """Dictionary of features in face
        """
        return self.fast_features()

    @property
    def confidence(self, outof=10.):
        """Calculates the confidence of the detection
        """
        return min(self.n, outof) / outof

    def fast_features(self):
        """Quickly generate facial features (no detection, just guessing)
        """
        def ffeat(name, x, y):
            return (
                name, {
                    "x": self.rect.x + self.rect.w * x,
                    "y": self.rect.y + self.rect.h * y
                }
            )
        return dict([
            ffeat("eye_left", 0.34, 0.39),
            ffeat("eye_right", 0.69, 0.39),
            ffeat("nose", 0.5, 0.66),
            ffeat("mouth_left", 0.40, 0.85),
            ffeat("mouth_center", 0.5, 0.85),
            ffeat("mouth_right", 0.59, 0.85),
        ])

    def dict(self):
        return dict(confidence=self.confidence,
                    rect=self.rect.dict(),
                    **self.features)
