#!/usr/bin/env python3
""" Basic Flask app Module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Configuration class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """Endpoint returning Hello world.
    """
    return render_template("7-index.html")


@babel.localeselector
def get_locale() -> str:
    """Select the best match language based on priority:
    URL param, user settings, request header, default.
    """

    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale

    if g.get('user', None):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Returns a user by their ID or None.
    """
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """"Sets the global user before each request.
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> str:
    """ Select the best match timezone based on priority:
        URL param, user settings, default to UTC.
    """
    requested_timezone = request.args.get('timezone')
    if requested_timezone:
        try:
            return pytz.timezone(requested_timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.get('user'):
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                return pytz.timezone(user_timezone).zone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return "UTC"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
