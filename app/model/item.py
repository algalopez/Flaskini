
class Item:
    def __init__(self, item_id, item_item, item_list):
        self.id: int = item_id
        self.item: str = item_item
        self.list: int = item_list

    def __repr__(self):
        return "<model.Item(id='%d', item='%s', list='%d')>" % (self.id, self.item, self.list)

    def __eq__(self, other):
        return isinstance(other, Item) and \
               self.id == other.id and \
               self.item == other.item and \
               self.list == other.list

