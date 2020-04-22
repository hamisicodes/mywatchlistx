from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# initialig application
app = Flask(__name__ , instance_relative_config = True)

# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# Initialising botstrap
bootstrap = Bootstrap(app)

from app import views     #import the views file from the app folder
from app import error