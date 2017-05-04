# -*- coding: utf-8 -*-

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
        pass