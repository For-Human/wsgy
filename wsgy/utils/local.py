# -*- coding: utf-8 -*-
import threading

class CTX(threading.local):
    pass

class Proxy(object):
    
    def __init__(self, ctx):
        self.ctx = ctx
        
    def __getattr__(self, key):
        return self.ctx.request.__getattribute__(key)