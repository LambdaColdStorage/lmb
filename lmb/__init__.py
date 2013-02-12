#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    λ
    ~

    :created: 2013-02-10 16:14:31 -0800
    :copyright: (c) 2013. Lambda Labs, Inc.
    :license: BSD. See LICENSE.
"""
import sys
import os
import lmb.server as server
import subprocess

__version__ = '0.1-dev'
__author__ = [
    "Stephen A. Balaban <s@lambdal.com>",
]

DEFAULT_PORT = 8080


def run(port=DEFAULT_PORT):
    server.run(port)


def kill_server():
    pid = str(os.getpid())
    p = subprocess.Popen(['kill', '-9', pid], stdout=subprocess.PIPE)
    sys.stderr.write('\nKilling server with PID: %s\n' % pid)
    out, err = p.communicate()



#os.system("your_command_here; second_command; third; etc")
