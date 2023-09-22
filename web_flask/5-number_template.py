#!/usr/bin/python3

"""Simple flask app"""

if __name__ == '__main__':
    # import module
    from flask import Flask, render_template

    # create instance of Flask class
    app = Flask(__name__)

    # specify routes with decorator
    @app.route("/", strict_slashes=False)
    def hello_hbnb():
        """ Displays Hello HBNB! """
        return ("Hello HBNB!")

    @app.route("/hbnb", strict_slashes=False)
    def hbnb():
        """Displays HBNB"""
        return ("HBNB")

    @app.route("/c/<text>", strict_slashes=False)
    def cisfun(text):
        """c is fun"""
        no_underscore = text.replace("_", " ")
        return (f"C {no_underscore}")

    @app.route('/python/', strict_slashes=False)
    @app.route("/python/<text>", strict_slashes=False)
    def python_is_cool(text='is cool'):
        """Python is cool"""
        no_underscore = text.replace("_", " ")
        return (f"Python {no_underscore}")

    @app.route('/number/<int:n>', strict_slashes=False)
    def check_int(n):
        """Check if number is integer"""
        # if type(n) is integer:
        return (f"{n} is a number")

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def check_int_html(n):
        """Check if number is integer"""
        # if type(n) is integer:
        return render_template('5-number.html', n=n)

    app.run(host='0.0.0.0', port=5000)
