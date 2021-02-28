import logging

from sqlalchemy.orm import Session

from app.model.list import List as ModelList
from app.repository import list_dao, database_connection


def run(request: int):
    """
    Get a list

    :param request: A list id
    :return: The list
    """
    session: Session = database_connection.get_session()
    try:
        logging.info('Creating new list')
        repository_list = list_dao.get_list(session, request)
        domain_list: ModelList = repository_list.map_to_domain() if repository_list is not None else None
    finally:
        session.close()

    return domain_list
