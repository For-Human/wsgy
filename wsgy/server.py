# -*- coding: utf-8 -*-

class Server(object):
    """Server is a wsgi server class.
    
    :param host: host
    :param port: port
    :param app: wsgi application
    """
    
    def __init__(self, host, port, app):
        import socket
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        self.socket.listen(5)
        
        self.host = host
        self.port = port
        self.app = app
        
    def serve_forever(self):
        import datetime
        
        while True:
            self.client_socket, self.client_address = self.socket.accept()
            self.request = self.client_socket.recv(1024)
            body = self.app(self.environ, self.start_response)
            
            print '[{time}] {host}:{port}'.format(
                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                host = self.client_address[0],
                port = self.client_address[1],
            )
            
            try:
                status, headers = self.response
                response = 'HTTP/1.1 {status}\r\n'.format(status=status)
                for header in headers:
                    response += '{0}: {1}\r\n'.format(*header)
                response += '\r\n'
                for data in body:
                    response += data
                self.client_socket.sendall(response)
            finally:
                self.client_socket.close()

    @property
    def environ(self):
        import os
        import sys
        import StringIO
        import urlparse
        
        request_lines = self.request.splitlines()
        method   = ''
        script   = ''
        path     = ''
        query    = ''
        protocol = ''
        headers  = {}
        
        if request_lines:
            tmp    = request_lines[0].split()
            method = tmp[0]
            parse  = urlparse.urlparse(tmp[1])
            path   = parse.path
            query  = parse.query
            
            if '.' in path:
                script = os.path.split(path)[-1]
            
            if len(tmp) == 3:
                protocol = tmp[2]
                
        if len(request_lines) > 1:
            for request_line in request_lines[1:]:
                kv = request_line.split(':')
                if len(kv) == 1:
                    break
                headers[kv[0]] = ':'.join(kv[1:])
        
        environ = {}
        environ['wsgi.version']      = (1, 0)
        environ['wsgi.url_scheme']   = 'http'
        environ['wsgi.input']        = StringIO.StringIO(self.request)
        environ['wsgi.errors']       = sys.stderr
        environ['wsgi.multithread']  = False
        environ['wsgi.multiprocess'] = False
        environ['wsgi.run_once']     = False
        environ['REQUEST_METHOD']    = method
        environ['SCRIPT_NAME']       = script
        environ['PATH_INFO']         = path
        environ['QUERY_STRING']      = query
        environ['CONTENT_TYPE']      = headers.get('Content-Type', '')
        environ['CONTENT_LENGTH']    = headers.get('Content-Length', '')
        environ['SERVER_NAME']       = self.host
        environ['SERVER_PORT']       = self.port.__str__()
        environ['SERVER_PROTOCOl']   = protocol
        
        return environ
        
    def start_response(self, status, headers):
        self.response = [status, headers]