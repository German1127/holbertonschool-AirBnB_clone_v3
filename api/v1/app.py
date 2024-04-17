#!/usr/bin/python3
"""
start a flask app
"""

from api.v1.views import app_views
from os import getenv
from models import storage
from flask import Flask

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def app_teardown():
    """method that calls storage.close"""
    storage.close()


if __name__=="__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host, port, threaded=True)
