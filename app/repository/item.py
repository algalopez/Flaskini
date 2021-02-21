from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class Item(declarative_base()):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    item = Column(String, unique=True)
    list = Column(Integer, ForeignKey('list.id'), nullable=False)

    def __repr__(self):
        return "<Item(id='%d', item='%s', list='%d')>" % (self.id, self.item, self.list)
