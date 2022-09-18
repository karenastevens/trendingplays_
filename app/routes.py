from crypt import methods
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from app import app
import mysql.connector
import os
from flask import (Blueprint, render_template, url_for)
from datetime import (datetime, timedelta)

bp = Blueprint('index', __name__, url_prefix='/')

my_conn=mysql.connector.connect(
    user = os.environ.get("DB_USER"),
    password = os.environ.get("DB_PASS"),
    db = os.environ.get("DB_NAME"),
    host = os.environ.get("DB_HOST"),
)


@bp.route("/", methods=['GET'])
def index():
    stylesheet = url_for('static', filename='styles/stylesheet.css')
    logo = url_for('static', filename='styles/Trending.png')
    favicon = url_for('static', filename='styles/T.png')
    mycursor = my_conn.cursor()
    mycursor.execute("SELECT Symbol, Count FROM nasdaq_tickers ORDER BY Count DESC LIMIT 10")
    rows = mycursor.fetchall()
    return render_template('index.html', stylesheet=stylesheet, logo=logo, favicon=favicon, rows=rows)
