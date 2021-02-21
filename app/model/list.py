
class List:
    def __init__(self, list_id, list_list):
        self.id = list_id
        self.list = list_list

    def __repr__(self):
        return "<model.List(id='%d', list='%s')>" % (self.id, self.list)
