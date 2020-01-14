from flask import Flask


def create_app():
    """Application Factory"""

    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import views
        return app
