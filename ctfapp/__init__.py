# Import stuff
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Define the WSGI application object
app = Flask(__name__)


# Configurations
app.config.from_object('config')

# Create db object
db = SQLAlchemy(app)

# Build the database:
# This will create the database file using SQLAlchemy
# and lets go
from . import model, views
