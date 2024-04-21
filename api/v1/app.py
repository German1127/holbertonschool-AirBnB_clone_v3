#!/usr/bin/python3
"""module using Flask"""
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
import os
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(self):
    """closes the storage on teardown"""
    return storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ handler for 404 errors """
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    """Main function of Flask app"""
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNH_API_PORT', 5000)),
            threaded=True, debug=False)
