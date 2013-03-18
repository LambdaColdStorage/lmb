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
import os
import cv
from utils import pil_path
from draw import pil_rect, pil_crop_rect
from PIL import ImageDraw


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dict(self):
        return {
            'x': self.x,
            'y': self.y
        }

    def to_tuple(self):
        return self.x, self.y


class Size(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def dict(self):
        return {
            'w': self.w,
            'h': self.h
        }

    def to_tuple(self):
        return self.w, self.h


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

    @property
    def size(self):
        if not hasattr(self, '_size'):
            self._size = Size(*self.img_pil.size)
        return self._size

    def cv_rep(self, depth=cv.IPL_DEPTH_8U, chan=1):
        """OpenCV representation of this image.
        """
        if not hasattr(self, '_cv_rep'):
            pc = self.img_pil.convert('L')
            cvi = cv.CreateImageHeader(pc.size, depth, chan)
            cv.SetData(cvi, pc.tostring())
            self.img_cv = cvi
            self._cv_rep = cvi
        return self._cv_rep

    def cv_mat(self, depth=cv.IPL_DEPTH_8U):
        if not hasattr(self, '_cv_mat'):
            self._cv_mat = cv.GetMat(self.cv_rep(depth=depth))
        return self._cv_mat

    def resize(self, size):
        """Img, size -> cvImg
        """
        result = cv.CreateMat(size.w, size.h, cv.CV_8UC1)
        cv.Resize(self.cv_mat(), result)
        return result

    def draw(self, rect):
        """Draws a rectangle on an image, changes made in place
        """
        draw = ImageDraw.Draw(self.img_pil)
        draw.rectangle(pil_rect(rect), fill=None, outline='green')
        return self

    def save(self, path):
        """Saves this image to disk at path.
        """
        typemap = {
            'JPG': 'JPEG'
        }
        ot = os.path.splitext(path)[1]
        ot = ot.split('.')[-1] if '.' in ot else ot
        if ot:
            self.img_pil.save(path, typemap.get(ot.upper(), ot))
        else:
            raise Exception("Couldn't find a valid image type in path: %s"
                            % path)

    def __add__(self, addend):
        """Add two images together -> cvImg
        """
        bmp = self.empty()
        if isinstance(addend, Img):
            cv.Add(self.cv_rep(), addend.cv_rep(), bmp)
        else:
            cv.AddS(self.cv_rep(), cv.Scalar(addend, addend, addend), bmp)
        return bmp

    def empty(self, depth=cv.IPL_DEPTH_8U, chan=3):
        """Creates an empty copy of this image
        """
        bmp = cv.CreateImage(self.size, depth, chan)
        cv.SetZero(bmp)
        return bmp

    def crop(self, rect):
        """Crops this image around the rect

        img, rect -> pil_img
        """
        rect = [int(float(x)) for x in rect]
        cropped_img = self.img_pil.crop(pil_crop_rect(rect))
        return cropped_img

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
            w = self.rect.w / 5.
            h = self.rect.h / 12.
            return (
                name, {
                    'x': self.rect.x + self.rect.w * x - w / 2.,
                    'y': self.rect.y + self.rect.h * y - h / 2.,
                    'w': w,
                    'h': h,
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
