from typing import List

from sqlalchemy.orm import Session

from app.repository.model.list import List as RepositoryList


def get_lists(session: Session) -> List[RepositoryList]:
    lists: List[RepositoryList] = session.query(RepositoryList).all()
    return lists


def get_list(session: Session, list_id) -> RepositoryList:
    repository_list: RepositoryList = session.query(RepositoryList).get(list_id)
    return repository_list


def create_list(session: Session, new_list: RepositoryList) -> RepositoryList:
    session.add(new_list)
    session.commit()
    return new_list


def update_list(session: Session, list_id, map_of_changes) -> RepositoryList:
    repository_list = session.query(RepositoryList).filter(RepositoryList.id == list_id).update(map_of_changes)
    session.commit()
    return repository_list


def remove_list(session: Session, list_id) -> None:
    element = session.query(RepositoryList).get(list_id)
    session.delete(element)
    session.commit()
