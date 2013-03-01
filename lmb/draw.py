#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    draw.py
    ~~~~~

    basic drawing functionality

    :created: 2013-02-24 22:49:07 -0800
    :copyright: (c) 2013, Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
from utils import new_name

OUTTYPE = 'PNG'


def pil_rect(rect_tup):
    """ x, y, w, h -> x, y, x, y
    """
    x, y, w, h = [float(f) for f in rect_tup]
    return (x, y), (x + w, y + h)


def draw_rect(img, rect_tup):
    """Draws a rectangle on an image, causes a side effect of  writing it to
    disk
    """
    img.draw(rect_tup)
    name = new_name(img.src)
    img.save(name)
    return name
