"""
The flask application package.
"""
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Configure logging for production use
if not app.debug:
    # Set the logging level
    app.logger.setLevel(logging.INFO)

    # Configure a rotating file handler to store logs
    file_handler = RotatingFileHandler(
        'flaskwebproject.log', maxBytes=10240, backupCount=10
    )
    file_handler.setLevel(logging.INFO)

    # Define log message format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)

    # Attach the handler to the app's logger
    app.logger.addHandler(file_handler)

    app.logger.info('Flask Web Project startup')

# Initialize Flask extensions
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Import views
import FlaskWebProject.views
