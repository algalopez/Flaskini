from app.repository import list_dao
from app.model.list import List as ModelList
from typing import List
import logging


def run(request):
    logging.info('Getting all lists')
    domain_lists: List[ModelList] = [repository_list.map_to_domain() for repository_list in list_dao.get_lists()]
    logging.debug('lists: %s' % domain_lists)
    return domain_lists

