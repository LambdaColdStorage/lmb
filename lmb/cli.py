#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    cli.py
    ~~~~~

    lmb command line interface toolchain

    examples uses:

    ```
    $ lmb detect faces.jpg
    10 10 128 128
    $ lmb detect face.jpg | lmb draw -i faces.jpg > faces_rect.jpg
    $ cat faces_rect.jpg | lmb edge > faces_rect_edge.jpg
    $ lmb gallery *.jpg > gallery.html
    ```

    :created: 2013-02-21 23:59:15 -0800
    :copyright: (c) 2013, Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""


def detect(*images):
    """Detect faces in images, output rects.

    Outputs serialized shapes
    """
    pass


def draw(shapes, image):
    """Draw shapes on an image (default rectangles)

    Outputs an imge
    """
    pass


def edge(img):
    """Perform edge detection on an image

    Outputs an image
    """
    pass


def gallery(*images):
    """Create an HTML gallery for the images provided.
    """
    pass
