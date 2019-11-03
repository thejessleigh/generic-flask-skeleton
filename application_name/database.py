import datetime
import os

from sqlalchemy import create_engine, func, Column, DateTime, Integer
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


class BaseModel(Base):
    """Base class from which all models should inherit.
    Provides primary key, updated, and created columns
    """

    __abstract__ = True
    id = Column(Integer, primary_key=True)
    updated = Column(DateTime, onupdate=datetime.datetime.now)
    created = Column(DateTime, server_default=func.now())
