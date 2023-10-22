#!/usr/bin/python3
""" Starting a Flask web application HBNB"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Printing a message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Printing a Message when /hbnb is called """
    return 'HBNB'

if __name__ == "__main__":
    """ My main function """
    app.run(host='0.0.0.0', port=5000)
