# wsgy

wsgy is a microframework for wsgi, and it has many features such as

- wsgy has a small wsgi server
- wsgy has a top-to-bottom design wsgi application
- wsgy is inspired by [flask](https://github.com/pallets/flask) and [awesome-python-webapp](https://github.com/michaelliao/awesome-python-webapp)
- wsgy supports `pip install wsgy` 

## Hello World

```python
from wsgy import Server, App

app = App(__name__)

@app.get('/index')
def index():
    return '<h1>Hello World!</h1>'
    
if __name__ == '__main__':
    httpd = Server('', 8888, app)
    httpd.serve_forever()
```

## example

- [example1](https://github.com/For-Human/wsgy/blob/master/example/example1/test.py)
- [example2](https://github.com/For-Human/wsgy/blob/master/example/example2/test.py)

## TODO

- support python3