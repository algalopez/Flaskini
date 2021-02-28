from app.actor import get_list
from app.model.item import Item as ModelItem
from app.model.list import List as ModelList
from test import database_helper


@database_helper.prepare_database(
    before=[
        'INSERT INTO list (id, list) VALUES (1, "list 1");',
        'INSERT INTO item (id, item, list) VALUES (1, "item 1", 1);'],
    after=[
        'DELETE FROM item WHERE id IN (1);',
        'DELETE FROM list WHERE id IN (1);'])
def test_get_list():
    result = get_list.run(1)

    expected_list = ModelList(list_id=1, list_list='list 1', list_items=[ModelItem(1, 'item 1', 1)])
    assert expected_list == result


def test_get_lists_when_no_lists():
    result = get_list.run(12)
    assert result is None
