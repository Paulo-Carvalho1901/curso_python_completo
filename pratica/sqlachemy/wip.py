from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry, Session
from sqlalchemy import create_engine, select


engine = create_engine('sqlite:///database.db')

reg = registry()

@reg.mapped_as_dataclass
class Comment:
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nama: Mapped[str]
    Comment: Mapped[str]
    live: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )


Comment(
    name='Paulo',
    comment='bla',
    live='youtube'
)


with Session(engine) as s:
    result = s.scalar(select(Comment).where(Comment.id == 1))
    s.delete(result)
    s.commit()
