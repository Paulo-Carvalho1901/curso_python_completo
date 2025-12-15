from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import declarative_base


class Base(declarative_base):
    ...


class Comment(Base):
    __tablename__ = 'comments'

    