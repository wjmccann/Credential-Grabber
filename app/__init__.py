import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Not-so-secret'
from app import routes

handler = RotatingFileHandler('creds.log', maxBytes=10000, backupCount=10)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
