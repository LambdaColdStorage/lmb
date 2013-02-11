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
    """
    Rectangle object
    """
    def __init__(self, x, y, w, h):
        self.origin = Point(x, y)
        self.size = Size(w, h)

    def __repr__(self):
        return self.dict()

    def dict(self):
        return dict(origin=self.origin.dict(),
                    size=self.size.dict())


class Img(object):
    """
    Core lambda labs image object
    """
    def __init__(self, src):
        self.src = src
        self.img_pil = pil_path(src)

    def cv_rep(self):
        """
        OpenCV representation of this image.
        """
        pc = self.img_pil.convert('L')
        cvi = cv.CreateImageHeader(pc.size, cv.IPL_DEPTH_8U, 1)
        cv.SetData(cvi, pc.tostring(), pc.size[0])
        self.img_cv = cvi
        return cvi
