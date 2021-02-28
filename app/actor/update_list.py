import logging
from typing import Dict, Union, Any

from sqlalchemy.orm import Session

from app.model.list import List as ModelList
from app.repository import list_dao, database_connection
from app.repository.model.list import List as RepositoryList


def run(request: Dict[Any, Union[int, ModelList]]):
    """
    Update a list

    :param request: A list id and the list to update its fields. Ex: {id: 1, list: List(...)}
    :return: The number of rows changed
    """
    logging.info('Updating a list')
    session: Session = database_connection.get_session()
    try:
        request_id, request_list = unfold_request(request)
        repository_list: RepositoryList = map_to_repository(request_list)
        dict_list = entity_as_dict(repository_list)
        result = list_dao.update_list(session, request_id, dict_list)
    finally:
        session.close()
    return result


def unfold_request(request):
    return request.get("id"), request.get("list")


def map_to_repository(model_list) -> RepositoryList:
    repository_list: RepositoryList = RepositoryList()
    repository_list.list = model_list.list
    return repository_list


def entity_as_dict(repository_list) -> Dict:
    dict_list = repository_list.__dict__
    dict_list.pop('_sa_instance_state', None)
    return dict_list

