import logging

from sqlalchemy.orm import Session

from app.model.list import List as ModelList
from app.repository import list_dao, database_connection
from app.repository.model.list import List as RepositoryList


def run(request: ModelList):
    """
    Create a new list

    :param request: A list
    :return: The recently created list
    """
    logging.info('Creating new list')
    session: Session = database_connection.get_session()
    try:
        repository_list: RepositoryList = map_to_repository(request)
        domain_list: ModelList = list_dao.create_list(session, repository_list).map_to_domain()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
    return domain_list


def map_to_repository(model_list) -> RepositoryList:
    repository_list: RepositoryList = RepositoryList()
    repository_list.list = model_list.list
    return repository_list
