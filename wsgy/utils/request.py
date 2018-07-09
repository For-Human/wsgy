# -*- coding: utf-8 -*-
from collections import defaultdict

class Request(object):
    
    def __init__(self, environ):
        self.environ = environ
    
    @property
    def method(self):
        return self.environ['REQUEST_METHOD']
    
    @property
    def path(self):
        return self.environ['PATH_INFO']
    
    @property
    def query(self):
        query = defaultdict(list)
        if self.environ['QUERY_STRING']:
            for q in self.environ['QUERY_STRING'].split('&'):
                kv = q.split('=')
                query[kv[0]].append(kv[1])
        return query
        
    @property
    def protocol(self):
        return self.environ['SERVER_PROTOCOL']
    
    @property
    def headers(self):
        return self.parse()[0]
    
    @property
    def body(self):
        return self.parse()[1]
    
    @property
    def form(self):
        form = defaultdict(list)
        if self.body:
            for d in self.body.split('&'):
                kv = d.split('=')
                form[kv[0]].append(kv[1])
        return form
        
    def parse(self):
        request = self.environ['wsgi.input'].getvalue()
        request_lines = request.splitlines()
        headers = {}
        body = ''
        
        index = 1
        if len(request_lines) > 1:
            for request_line in request_lines[1:]:
                index += 1
                kv = request_line.split(':')
                if len(kv) == 1:
                    break
                headers[kv[0]] = ':'.join(kv[1:])
                
        if len(request_lines) > index:
            body = request_lines[index]
            
        return headers, body