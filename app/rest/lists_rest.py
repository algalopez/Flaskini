from flask import Blueprint, Response
from app.actor import get_all_lists
import jsonpickle

lists_resource = Blueprint('lists_resource', __name__)


@lists_resource.route('/rest/lists', methods=['GET'])
def get_all():
    return jsonpickle.encode(get_all_lists.run(None), unpicklable=False)


@lists_resource.route('/rest/lists/<int:list_id>', methods=['GET'])
def get(list_id):
    return Response('{"error":"Not implemented", "id": %s}' % list_id, status=501, mimetype='application/json')


@lists_resource.route('/rest/lists', methods=['POST'])
def post():
    return Response('{"error":"Not implemented"}', status=501, mimetype='application/json')


@lists_resource.route('/rest/lists/<int:list_id>', methods=['PUT'])
def put(list_id):
    return Response('{"error":"Not implemented", "id": %s}' % list_id, status=501, mimetype='application/json')


@lists_resource.route('/rest/lists/<int:list_id>', methods=['DELETE'])
def delete(list_id):
    return Response('{"error":"Not implemented", "id": %s}' % list_id, status=501, mimetype='application/json')


