#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
        Setup for tests. Start the server.

        :copyright: (c) by Lambda Labs, Inc.
        :license: BSD. See LICENSE.
"""
import lmb
DEFAULT_PORT = 8080

# setup the rest server at localhost:DEFAULT_PORT
lmb.run(DEFAULT_PORT)
