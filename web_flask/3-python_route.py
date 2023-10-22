#!/usr/bin/python3
""" Starting a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returning Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returning HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """displaying “C ” followed by the value of
the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """displaying “Python ”, followed by the value of
the text variable"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    """ My main function """
    app.run(host='0.0.0.0', port='5000')
