# -*- coding: utf-8 -*-
import threading

class CTX(threading.local):
    pass

class RequestProxy(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def __getattribute__(self, key):
        ctx = super(RequestProxy, self).__getattribute__("ctx")
        return ctx.request.__getattribute__(key)