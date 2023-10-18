from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/math', methods=['GET', 'POST'])
def math_operation():
    if request.method == "POST":
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num1'])

        if (ops == 'add'):
            result = num1+num2
            
        elif (ops == "subtract"):
            result = num1 - num2
            
        elif (ops == "multiply"):
            result = num1 * num2
            
        elif (ops == "divide"):
            result = num1 / num2
        
        return render_template('result.html', result=result)

@app.route('/postman_data', methods=['POST'])
def math_operation2():
    if request.method == "POST":
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num1'])

        if (ops == 'add'):
            result = num1+num2
            
        elif (ops == "subtract"):
            result = num1 - num2
            
        elif (ops == "multiply"):
            result = num1 * num2
            
        elif (ops == "divide"):
            result = num1 / num2
        
        return jsonify(result)

# @app.route('/hello_world1')
# def hello_world1():
#     return '<h1>Hello, world 1</h1>'

# @app.route("/query_url")
# def input_function():
#     data = request.args.get('x')
#     return "This is a data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host='0.0.0.0')
