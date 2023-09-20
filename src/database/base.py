from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

import config

engine = create_engine(config.DATABASE_CONNECT_STRING, echo=True)


class Base(DeclarativeBase):
    pass
