from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, Unicode, Integer
from sqlalchemy.orm import relationship

from app.model.list import List as ModelList
from app.repository.database_connection import BASE
from app.repository.model.item import Item


@dataclass
class List(BASE):
    __tablename__ = "list"
    id: int = Column(Integer, primary_key=True)
    list: str = Column(Unicode)
    items: List[Item] = relationship("Item", lazy='joined')

    def map_to_domain(self) -> ModelList:
        return ModelList(self.id, self.list, list(map(lambda i: i.map_to_domain(), self.items)))

