#!/usr/bin/python3

"""Simple flask app"""

if __name__ == '__main__':
    # import module
    from flask import Flask

    # create instance of Flask class
    app = Flask(__name__)

    # specify routes with decorator
    @app.route("/", strict_slashes=False)
    def hello_hbnb():
        """ Displays Hello HBNB! """
        return ("Hello HBNB!")

    app.run(host='0.0.0.0', port=5000)
