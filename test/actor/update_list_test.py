from app.actor import update_list
from app.model.list import List as ModelList
from test import database_helper


@database_helper.prepare_database(
    before=['INSERT INTO list (id, list) VALUES (1, "list 1");'],
    after=['DELETE FROM list WHERE id IN (1);'])
def test_remove_list():
    new_list = ModelList(list_id=1, list_list='new list', list_items=None)
    result = update_list.run({"id": 1, "list": new_list})

    elements = database_helper.query_one('SELECT COUNT(*) FROM list;')

    assert elements[0] == 1
    assert result == 1
