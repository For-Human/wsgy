# -*- coding: utf-8 -*-
from wsgy import Server, App, request, render_template

app = App(__name__)

@app.get('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    httpd = Server('', 8888, app)
    httpd.serve_forever()