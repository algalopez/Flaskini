from dataclasses import dataclass

from sqlalchemy import Column, Integer, ForeignKey, Unicode

from app.model.item import Item as ModelItem
from app.repository.database_connection import BASE


@dataclass
class Item(BASE):
    __tablename__ = "item"
    id: int = Column(Integer, primary_key=True)
    item: str = Column(Unicode, unique=True)
    list: int = Column(Integer, ForeignKey('list.id'), nullable=False)

    def map_to_domain(self) -> ModelItem:
        return ModelItem(self.id, self.item, self.list)
