#!/usr/bin/env python3
""" task 1 module
"""
from flask import Flask
from flask_babel import Babel


class Config:
    """ configration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index():
    """ the main page
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
