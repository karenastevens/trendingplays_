from flask import Flask
import os

app = Flask(__name__)
from app import routes
app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
app.register_blueprint(routes.bp)
# prevent cached response
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
