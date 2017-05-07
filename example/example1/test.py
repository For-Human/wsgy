# -*- coding: utf-8 -*-
from wsgy import Server, App, request, render_template

app = App(__name__)

@app.get('/')
def index():
    return render_template('index.html')
    
@app.post('/')
def summary():
    sex = request.form['sex'][0]
    age = request.form['age'][0]
    return render_template('summary.html', sex=sex, age=age)

if __name__ == '__main__':
    httpd = Server('', 8888, app)
    httpd.serve_forever()