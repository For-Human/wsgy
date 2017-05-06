# -*- coding: utf-8 -*-

class Template(object):
    
    def __init__(self, t):
        self.t = t
   
    def render(self, **kwargs):
        return self.t.format(**kwargs)