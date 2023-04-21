import pytest

from sqlalchemy import JSON
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from sqlalchemy import create_engine

engine = create_engine("sqlite:///sqlite.db", connect_args={"check_same_thread": False})


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = "test"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    json: Mapped[JSON]


def create_all_table():
    Base.metadata.create_all(bind=engine)


create_all_table()
