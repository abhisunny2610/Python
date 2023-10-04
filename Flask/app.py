from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello, World</h1>"

@app.route('/hello_world1')
def hello_world1():
    return '<h1>Hello, world 1</h1>'

@app.route("/query_url")
def input_function():
    data = request.args.get('x')
    return "This is a data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host='0.0.0.0')
