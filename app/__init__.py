from flask import Flask
from decouple import config
from logging import Formatter, INFO
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
app.config.from_object(config)
from app import routes, errors

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/eyeoveryour.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(INFO)
app.logger.info('Starting application.')
