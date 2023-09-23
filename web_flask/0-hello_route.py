#!/usr/bin/python3
"""starts flask server"""


from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """route shows Hello HBNB"""
    return "Hello HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
