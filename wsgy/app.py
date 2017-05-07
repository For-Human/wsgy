# -*- coding: utf-8 -*-
from .utils import Request, Response, CTX, Proxy, Template

ctx = CTX()
request = Proxy(ctx)

class App(object):
    
    def __init__(self):
        self.routes = []
    
    def get(self, rule):
        def wrapper(func):
            self.routes.append(('GET', rule, func))
            return func
        return wrapper
        
    def post(self, rule):
        def wrapper(func):
            self.routes.append(('POST', rule, func))
            return func
        return wrapper
        
    def head(self, rule):
        def wrapper(func):
            self.routes.append(('HEAD', rule, func))
            return func
        return wrapper
        
    def put(self, rule):
        def wrapper(func):
            self.routes.append(('PUT', rule, func))
            return func
        return wrapper
        
    def delete(self, rule):
        def wrapper(func):
            self.routes.append(('DELETE', rule, func))
            return func
        return wrapper
    
    def __call__(self, environ, start_response):
        import re
        
        r = None
        ctx.request = Request(environ)
        for method, rule, func in self.routes:
            if method == ctx.request.method:
                m = re.match('^' + rule + '$', ctx.request.path)
                if m:
                    args = m.groups()
                    r = func(*args)
                    break
        
        if isinstance(r, basestring):
            response = Resposne(r)
        elif isinstance(r, tuple):
            response = Response(*r)
        else:
            response = Response('<h1>404 Not Found</h1>', 404)
            
        start_response(response.status, response.headers)
        return response.body