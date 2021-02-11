import os

from flask import Flask, render_template

from src.models.kanye_rest_api import KanyeRestApi
from src.models.random_cat_api import RandomCatApi


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple index page
    @app.route("/")
    def index():
        kanye_rest_api = KanyeRestApi()
        random_cat_api = RandomCatApi()
        context = {
            "quote": kanye_rest_api.get_kanye_quote(),
            "img": random_cat_api.get_cat_img(),
        }
        return render_template("index.html", context=context)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    return app
