import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base

from saturnv.api.configuration import DatabaseConfiguration


engine = sqlalchemy.create_engine(DatabaseConfiguration.get_engine_url())
Base = declarative_base(engine)

Session = sqlalchemy.orm.sessionmaker(engine)
