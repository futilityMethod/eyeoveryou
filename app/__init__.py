from flask import Flask
from decouple import config

app = Flask(__name__)
app.config.from_object(config)
from app import routes
