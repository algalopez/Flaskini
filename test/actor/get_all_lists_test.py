from app.actor import get_all_lists
from test import database_helper
import logging
import pytest


@pytest.fixture(autouse=True)
def run_around_tests():
    logging.debug('Before')
    yield
    logging.debug('After')


@database_helper.prepare_database(
    before=[
        'INSERT INTO list (id, list) VALUES (1, "list 1");',
        'INSERT INTO list (id, list) VALUES (2, "list 2");'],
    after=['DELETE FROM list WHERE id IN (1,2);'])
def test_get_lists():
    lists = sorted(get_all_lists.run(None), key=lambda x: x.id)
    assert 2 == len(lists)
    assert 1 == lists[0].id
    assert 'list 1' == lists[0].list
    assert 2 == lists[1].id
    assert 'list 2' == lists[1].list


def test_get_lists_when_no_lists():
    lists = get_all_lists.run(None)
    assert 0 == len(lists)
