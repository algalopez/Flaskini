from flask import Flask
import configuration
from app.repository import database_connection
from app.rest import hello_rest, lists_rest

import logging

app = Flask(__name__)
appConfig = configuration.read_file('app.yaml')


def add_resources_endpoints():
    app.register_blueprint(hello_rest.hello_resource)
    app.register_blueprint(lists_rest.lists_resource)


def set_logger_format():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)-8s > %(message)s", datefmt="%I:%M:%S")


if __name__ == '__main__':
    add_resources_endpoints()
    set_logger_format()
    database_connection.start_database()
    app.run(host='0.0.0.0', port=appConfig.get('port'), debug=True)
