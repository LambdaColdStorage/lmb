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
import sys
import json
import threading

urls = (
    '/', 'hello',
    '/detect', 'detect',
)
app = web.application(urls, globals())

def response(obj):
    web.header('Content-Type', 'application/json')
    return json.dumps({
        'status': 'success',
        'result': obj
    }, indent=4)

class hello:
    def GET(self):
        return response(None)

class detect:
    def GET(self):
#        result = detect.detect_faces(url)
        result = [{}]
        return response(result)


def run(port=8080, address='0.0.0.0'):
    a_p = (address, port)
    threading.Thread(target=web.httpserver.runsimple, args=(app.wsgifunc(), a_p)).start()

if __name__ == "__main__":
    run()
