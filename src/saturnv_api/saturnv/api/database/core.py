import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base


class Configuration:

    username = 'saturnv'
    password = 'saturnv'
    hostname = 'localhost'
    port = '5432'
    database = 'saturnv'

    @staticmethod
    def get_engine_url(username=username, password=password, hostname=hostname, port=port, database=database):
        return f'postgresql://{username}:{password}@{hostname}:{port}/{database}'


engine = sqlalchemy.create_engine(Configuration.get_engine_url())
Base = declarative_base(engine)

Session = sqlalchemy.orm.sessionmaker(engine)
