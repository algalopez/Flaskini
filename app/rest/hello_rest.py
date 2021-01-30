from flask import Blueprint
from app.actor import get_hello
import jsonpickle

hello_resource = Blueprint('simple_page', __name__)


@hello_resource.route('/hello/', defaults={'name': 'world'})
@hello_resource.route('/hello/<name>')
def get(name):
    return jsonpickle.encode(get_hello.run(name), unpicklable=False)


