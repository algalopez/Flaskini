from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.model.list import List as ModelList


class List(declarative_base()):
    __tablename__ = "list"
    id = Column(Integer, primary_key=True)
    list = Column(String)
    # item = relationship("Item", back_populates="item")

    def map_to_domain(self) -> ModelList:
        return ModelList(self.id, self.list)

    def __repr__(self):
        return "<repository.List(id='%d', list='%s')>" % (self.id, self.list)
