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
import os
from PIL import ImageDraw

OUTTYPE = 'PNG'


def pil_rect(rect_tup):
    """ x, y, w, h -> x, y, x, y
    """
    x, y, w, h = [float(f) for f in rect_tup]
    return (x, y), (x + w, y + h)


def draw_name(src):
    head, tail = os.path.split(src)
    pwd = os.getcwd()
    return os.path.join(pwd, 'draw_' + tail)


def draw_rect(img, rect_tup):
    """Draws a rectangle on an image
    """
    pi = img.img_pil
    draw = ImageDraw.Draw(pi)
    draw.rectangle(pil_rect(rect_tup), fill=None, outline='green')
    name = draw_name(img.src)
    pi.save(name, OUTTYPE)
    return name
