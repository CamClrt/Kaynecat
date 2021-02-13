import os

from flask import Flask, render_template

from src.models.kanye_rest_api import KanyeRestApi
from src.models.random_cat_api import RandomCatApi


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=os.environ.get("SECRET_KEY") or "dev")

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
