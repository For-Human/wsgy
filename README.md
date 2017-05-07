# wsgy

## Hello World

```python
from wsgy import Server, App, request, render_template

app = App(__name__)

@app.get('/index')
def index():
    return '<h1>Hello World!</h1>'
    
if __name__ == '__main__':
    httpd = Server('', 8888, app)
    httpd.serve_forever()
```

## example

- [example1]()
- [example2]()

## API

## TODO