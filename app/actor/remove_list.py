import logging

from sqlalchemy.orm import Session

from app.repository import list_dao, database_connection


def run(request: int):
    """
    Remove a list

    :param request: A list id
    :return: None
    """
    logging.info('Removing a list')
    session: Session = database_connection.get_session()
    try:
        list_dao.remove_list(session, request)
    finally:
        session.close()
