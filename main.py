from flask import Flask
from app.repository import database_connection
from app.rest import hello_rest, lists_rest
from app.web import hello_web
from app import configuration

import logging


def add_resources_endpoints(flask_app):
    flask_app.register_blueprint(hello_rest.hello_resource)
    flask_app.register_blueprint(lists_rest.lists_resource)
    flask_app.register_blueprint(hello_web.hello_web)


def set_logger_format():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)-8s > %(message)s", datefmt="%I:%M:%S")


def load_database():
    from app.repository.model.list import List # noqa
    from app.repository.model.item import Item # noqa
    database_connection.load()


def start():
    set_logger_format()
    app_config = configuration.load(configuration.APP_CONFIG)
    flask_app = Flask(__name__)
    flask_app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    add_resources_endpoints(flask_app)
    load_database()
    flask_app.run(host='0.0.0.0', port=app_config.get('port'), debug=True)


if __name__ == '__main__':
    start()
