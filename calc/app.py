# Put your app in here.
from operations import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_request():
    b = int(request.args.get('b'))
    a = int(request.args.get('a'))
    return f"{add(a,b)}"

@app.route('/sub', methods=['GET'])
def sub_request():
    b = int(request.args.get('b'))
    a = int(request.args.get('a'))
    return f"{sub(a,b)}"

@app.route('/mult', methods=['GET'])
def mult_request():
    b = int(request.args.get('b'))
    a = int(request.args.get('a'))
    return f"{mult(a,b)}"

@app.route('/div', methods=['GET'])
def div_request():

    b = int(request.args.get('b'))
    a = int(request.args.get('a'))
    return f"{div(a,b)}"

operators = {'add':add, 'sub':sub, 'mult': mult, 'div':div}

@app.route("/math/<operator>")
def find_func(operator):
    operator = operators[operator]
    b = int(request.args.get('b'))
    a = int(request.args.get('a')) 
    return f"{operator(a,b)}"