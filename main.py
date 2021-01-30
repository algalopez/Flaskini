from flask import Flask
from flask_restful import Api
import configuration
from app.rest.hello_rest import hello_resource

app = Flask(__name__)
api = Api(app)
appConfig = configuration.read_file('app.yaml')


def add_resources_endpoints():
    app.register_blueprint(hello_resource)


if __name__ == '__main__':
    add_resources_endpoints()
    app.run(host='0.0.0.0', port=appConfig.get('port'), debug=True)
