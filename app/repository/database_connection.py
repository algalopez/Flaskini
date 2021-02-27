import sqlalchemy
from sqlalchemy.orm import sessionmaker
import logging
from app import registry, configuration
from sqlalchemy.ext.declarative import declarative_base

REGISTRY_NAME = 'database_engine'
BASE_NAME = "database_base"
BASE = declarative_base()


def load():
    logging.info(f"Loading database engine")

    database_config = registry.get(configuration.REGISTRY_NAME).get('database')

    user = database_config.get('user')
    password = database_config.get('password')
    host = database_config.get('host')
    port = database_config.get('port')
    database = database_config.get('database')
    engine = sqlalchemy.create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
    BASE.metadata.bind = engine
    registry.register(REGISTRY_NAME, engine)
    return engine


def get_session():
    engine = registry.get(REGISTRY_NAME)
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
