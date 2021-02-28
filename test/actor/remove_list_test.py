from app.actor import remove_list
from test import database_helper


@database_helper.prepare_database(
    before=['INSERT INTO list (id, list) VALUES (1, "list 1");'],
    after=[])
def test_remove_list():
    remove_list.run(1)

    elements = database_helper.query_one('SELECT COUNT(*) FROM list;')

    assert elements[0] == 0
