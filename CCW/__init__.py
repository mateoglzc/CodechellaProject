from flask import Flask
from CCW import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

from CCW import routes