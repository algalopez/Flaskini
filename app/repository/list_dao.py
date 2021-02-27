from typing import List

from app.repository import database_connection
from app.repository.model.list import List as RepositoryList


def get_lists() -> List[RepositoryList]:
    session = database_connection.get_session()
    lists = session.query(RepositoryList).all()
    session.close()
    return lists

# new_rec = Orders(ShipName="placeholder", ShipCountry="USA")
# session.add(new_rec)
# session.commit()
#
# updated_rec = session.query(Orders).filter_by(SOME_ID_COLUMN="SOME_ID_VALUE").first()
# updated_rec.ShipCountry = "USA"
# session.commit()
#
# deleted_rec = session.query(Orders).filter_by(SOME_ID_COLUMN="SOME_ID_VALUE").first()
# session.delete(deleted_rec)
# session.commit()
