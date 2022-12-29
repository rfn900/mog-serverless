from flask import Flask
from flask_cors import CORS
from api import commissions, forms, home, auth, services
from utils.logger import logger


def create_app():
    # create app instance
    app = Flask(__name__)

    logger.propagate = False
    # Configure cors policy
    CORS(app)

    # TODO
    # Initialize db

    # Register blueprints
    app.register_blueprint(commissions.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(services.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(forms.bp)

    return app
