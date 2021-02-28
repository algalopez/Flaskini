import logging

import pytest

from app.actor import get_all_lists
from app.model.item import Item as ModelItem
from app.model.list import List as ModelList
from test import database_helper


@pytest.fixture(autouse=True)
def run_around_tests():
    logging.debug('Before')
    yield
    logging.debug('After')


@database_helper.prepare_database(
    before=[
        'INSERT INTO list (id, list) VALUES (1, "list 1");',
        'INSERT INTO list (id, list) VALUES (2, "list 2");',
        'INSERT INTO item (id, item, list) VALUES (1, "item 1", 1);'],
    after=[
        'DELETE FROM item WHERE id IN (1);',
        'DELETE FROM list WHERE id IN (1, 2);'])
def test_get_lists():
    lists = sorted(get_all_lists.run(None), key=lambda x: x.id)

    expected_lists = [
        ModelList(list_id=1, list_list='list 1', list_items=[ModelItem(1, 'item 1', 1)]),
        ModelList(list_id=2, list_list='list 2', list_items=[])
    ]
    assert expected_lists == lists


def test_get_lists_when_no_lists():
    lists = get_all_lists.run(None)
    assert 0 == len(lists)
