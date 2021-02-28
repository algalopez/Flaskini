from app.actor import create_list
from app.model.list import List as ModelList
from test import database_helper


def test_create_list():
    new_list = ModelList(list_id=None, list_list='new list', list_items=None)
    result = create_list.run(new_list)

    database_helper.connect_to_database()
    created_list = database_helper.query_one(f"SELECT id, list FROM list WHERE id = {result.id};")
    database_helper.execute(f"DELETE FROM list WHERE id = {result.id};")
    database_helper.disconnect_from_database()

    assert created_list[0] > 0
    assert created_list[1] == 'new list'
    assert result.id > 0
    assert result.list == 'new list'
    assert result.items == []
