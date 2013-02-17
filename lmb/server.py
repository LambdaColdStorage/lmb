#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    sever.py - the web server
    ~~~~~~~~

    In addition to our command line utilities. LMB offers a familar HTTP
    interface to all of our calls.

    :created: 2013-02-10 16:15:25 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
import web
import web.httpserver
import json
import threading
import detect
import collections

urls = (
    '/', 'Hello',
    '/detect', 'Detect',
)
app = web.application(urls, globals())


def serialize(o):
    if isinstance(o, collections.Iterable):
        return [serialize(t) for t in o]
    if hasattr(o, 'dict'):
        return o.dict()
    return {}


def response(obj, rkey='images'):
    web.header('Content-Type', 'application/json')
    return json.dumps({
        'status': 'success',
        '%s' % rkey: serialize(obj)
    }, indent=4)


class Hello:
    def GET(self):
        return response(None)


class Detect:
    def GET(self):
        urls_str = web.input(urls='').urls
        urls = urls_str.split(',') if urls_str else []
        images = [detect.img_url(url) for url in urls if url]
        return response(images, 'images')


def run(port=8080, address='0.0.0.0'):
    a_p = (address, port)
    threading.Thread(target=web.httpserver.runsimple,
                     args=(app.wsgifunc(), a_p)).start()


if __name__ == "__main__":
    run()
