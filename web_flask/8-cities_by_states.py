#!/usr/bin/python3
"""starts flask server"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities_by_states route"""
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
