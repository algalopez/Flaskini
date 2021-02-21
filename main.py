from flask import Flask
from app.repository import database_connection
from app.rest import hello_rest, lists_rest
from app import configuration

import logging


def add_resources_endpoints(flask_app):
    flask_app.register_blueprint(hello_rest.hello_resource)
    flask_app.register_blueprint(lists_rest.lists_resource)


def set_logger_format():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)-8s > %(message)s", datefmt="%I:%M:%S")


def start():
    set_logger_format()
    app_config = configuration.load(configuration.APP_CONFIG)
    flask_app = Flask(__name__)
    add_resources_endpoints(flask_app)
    database_connection.load()
    flask_app.run(host='0.0.0.0', port=app_config.get('port'), debug=True)


if __name__ == '__main__':
    start()
