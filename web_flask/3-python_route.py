#!/usr/bin/python3
"""starts flask server"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """route shows Hello HBNB"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """route shows HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    _str = str(text).replace('_', ' ')
    return "C " + _str


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    _str = str(text).replace('_', ' ')
    return "Python " + _str


if __name__ == "__main__":
    app.run(host="0.0.0.0")
