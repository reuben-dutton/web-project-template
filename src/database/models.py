from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import config

engine = create_engine(config.DATABASE_CONNECT_STRING)
Base = declarative_base()
Base.metadata.reflect(engine)


# This represents a table
class Person(Base):
    __table__ = Base.metadata.tables["persons"]
