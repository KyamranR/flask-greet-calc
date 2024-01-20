# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def math_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = add(a,b)

    return str(results)

@app.route('/sub')
def math_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = sub(a,b)

    return str(results)

@app.route('/mult')
def math_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = mult(a,b)

    return str(results)

@app.route('/div')
def math_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = div(a,b)

    return str(results)

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = operations[operation](a,b)

    return str(results)


