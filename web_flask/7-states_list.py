#!/usr/bin/python3
"""starts flask server"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states_list route"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
