from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import declarative_base


class Base(declarative_base):
    ...


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    Comment = Column(String, nullable=False)
    live = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self) -> str:
        return f'comment({self.id=}, {self.name=}, {self.comment=}, {self.live=}, {self.created_at=})'
    