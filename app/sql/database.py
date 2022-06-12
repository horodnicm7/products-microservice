from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils.configuration import Configuration


class Database(object):
    _sqlalchemy_database_url = None
    _engine = None
    _session = None
    _base = declarative_base()

    _config = Configuration()

    @staticmethod
    def base():
        return Database._base

    @staticmethod
    def sqlalchemy_database_url():
        if Database._sqlalchemy_database_url is None:
            Database._sqlalchemy_database_url = "postgresql://{user}:{password}@{host}/{database_name}".format(
                user=Database._config.DATABASE_USER,
                password=Database._config.DATABASE_PASSWORD,
                host=Database._config.DATABASE_URL,
                database_name=Database._config.DATABASE_NAME
            )
        return Database._sqlalchemy_database_url

    @staticmethod
    def engine():
        if Database._engine is None:
            Database._engine = create_engine(Database.sqlalchemy_database_url())
        return Database._engine

    @staticmethod
    def session():
        if Database._session is None:
            Database._session = sessionmaker(autocommit=False, autoflush=False, bind=Database.engine())
        return Database._session
