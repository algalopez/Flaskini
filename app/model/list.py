from typing import List as List_type

from app.model.item import Item


class List:

    def __init__(self, list_id, list_list, list_items):
        self.id: int = list_id
        self.list: str = list_list
        self.items: List_type[Item] = list_items

    def __repr__(self):
        return "<model.List(id='%d', list='%s', items=%s)>" % (self.id, self.list, str(self.items))

    def __eq__(self, other):
        return isinstance(other, List) and \
               self.id == other.id and \
               self.list == other.list and \
               len(self.items) == len(other.items) and \
               all(i in self.items for i in other.items)
