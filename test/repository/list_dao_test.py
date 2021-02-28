import logging

from sqlalchemy.orm import Session

from app.repository import list_dao, database_connection
from app.repository.model.list import List as RepositoryList
from test import database_helper


@database_helper.prepare_database(
    before=[
        'INSERT INTO list (id, list) VALUES (1, "list 1");',
        'INSERT INTO list (id, list) VALUES (2, "list 2");',
        'INSERT INTO item (id, item, list) VALUES (1, "item 1", 1);'],
    after=[
        'DELETE FROM item WHERE id IN (1);',
        'DELETE FROM list WHERE id IN (1, 2);'])
def test_get_lists():
    session: Session = database_connection.get_session()
    lists = sorted(list_dao.get_lists(session), key=lambda x: x.id)

    logging.info(lists)

    assert 2 == len(lists)

    assert 1 == lists[0].id
    assert 'list 1' == lists[0].list
    assert 1 == len(lists[0].items)
    assert 1 == lists[0].items[0].id
    assert 'item 1' == lists[0].items[0].item
    assert 1 == lists[0].items[0].list

    assert 2 == lists[1].id
    assert 'list 2' == lists[1].list
    assert 0 == len(lists[1].items)
    session.close()


@database_helper.prepare_database(
    before=['INSERT INTO list (id, list) VALUES (1, "list 1"), (2, "list 2");'],
    after=['DELETE FROM list WHERE id IN (1, 2);'])
def test_get_list():
    session: Session = database_connection.get_session()
    list_2 = list_dao.get_list(session, 2)
    assert list_2.id == 2
    assert list_2.list == 'list 2'
    assert list_2.items == []
    session.close()


@database_helper.prepare_database(
    before=['INSERT INTO list (id, list) VALUES (1, "list 1"), (2, "list 2");'],
    after=['DELETE FROM list WHERE id IN (1, 2);'])
def test_remove_list():
    session: Session = database_connection.get_session()
    list_dao.remove_list(session, 1)
    result = database_helper.query_all('SELECT id, list FROM list;')
    assert len(result) == 1
    assert result[0][0] == 2
    assert result[0][1] == 'list 2'
    session.close()


def test_insert_list():
    session: Session = database_connection.get_session()
    repository_list: RepositoryList = RepositoryList()
    repository_list.list = 'list 123'
    list_dao.create_list(session, repository_list)
    database_helper.connect_to_database()
    result = database_helper.query_all('SELECT id, list FROM list;')

    database_helper.execute(f"DELETE FROM list WHERE id = {result[0][0]};")
    database_helper.disconnect_from_database()

    assert len(result) == 1
    assert result[0][0] > 0
    assert result[0][1] == 'list 123'
    session.close()


@database_helper.prepare_database(
    before=['INSERT INTO list (id, list) VALUES (1, "list 1");'],
    after=['DELETE FROM list WHERE id IN (1);'])
def test_update_list():
    session: Session = database_connection.get_session()
    list_dao.update_list(session, 1, {'list': 'new list'})
    result = database_helper.query_one('SELECT id, list FROM list WHERE id = 1;')

    assert result[0] == 1
    assert result[1] == 'new list'
    session.close()
