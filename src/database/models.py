import datetime
from typing import List

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.database.base import Base


association_table = Table(
    "association_table",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("actor_id", ForeignKey("actors.id"), primary_key=True),
)


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    release_date: Mapped[datetime.datetime] = mapped_column()
    actors: Mapped[List["Actor"]] = relationship(
        secondary=association_table, back_populates="movies"
    )

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date


class Actor(Base):
    __tablename__ = "actors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    birthday: Mapped[datetime.datetime] = mapped_column()
    movies: Mapped[List["Movie"]] = relationship(
        secondary=association_table, back_populates="actors"
    )

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
