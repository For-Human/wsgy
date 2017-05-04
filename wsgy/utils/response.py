#-*- coding: utf-8 -*-

class Response(object):
    
    def __init__(self, status, headers, datas):
        self.status  = status
        self.headers = headers
        self.datas   = datas