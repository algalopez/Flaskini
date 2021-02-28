import logging
from typing import List

from sqlalchemy.orm import Session

from app.model.list import List as ModelList
from app.repository import list_dao, database_connection


def run(request):
    """
    Get all lists

    :param request: None
    :return: A list of the existing lists
    """
    logging.info('Getting all lists')
    session: Session = database_connection.get_session()
    try:
        domain_lists: List[ModelList] = [repository_list.map_to_domain() for repository_list in
                                         list_dao.get_lists(session)]
        logging.debug('lists: %s' % domain_lists)
    finally:
        session.close()
    return domain_lists
