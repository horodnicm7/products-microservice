from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database(object):
    def __init__(self, config):
        self.config = config
        self.__create_database_connection()

    @staticmethod
    def base():
        return declarative_base()

    @property
    def session(self):
        return self._session_local

    def __create_database_connection(self):
        # sqlalchemy_database_url = "postgresql://user:password@postgresserver/db"
        sqlalchemy_database_url = "postgresql://{user}:{password}@{host}/{database_name}".format(
            user=self.config.DATABASE_USER,
            password=self.config.DATABASE_PASSWORD,
            host=self.config.DATABASE_URL,
            database_name=self.config.DATABASE_NAME
        )

        engine = create_engine(sqlalchemy_database_url, connect_args={"check_same_thread": False})

        self._session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
