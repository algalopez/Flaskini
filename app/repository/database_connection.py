import sqlalchemy
from sqlalchemy.orm import sessionmaker
import logging

# engine: sqlalchemy.engine.Engine
engine = None


def start_database():
    global engine
    engine = sqlalchemy.create_engine('mysql+pymysql://user:pass@127.0.0.1:3306/flaskini')
    logging.debug('database tables: %s' % engine.table_names())


def get_session():
    global engine
    if engine is None:
        start_database()
    factory = sessionmaker(bind=engine)
    return factory()


def close_session(session):
    session.close()

# def run_my_program():
#     session = Session()
#     try:
#         ThingOne().go(session)
#         ThingTwo().go(session)
#
#         session.commit()
#     except:
#         session.rollback()
#         raise
#     finally:
#         session.close()
