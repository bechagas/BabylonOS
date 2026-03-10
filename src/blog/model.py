from sqlalchemy import String, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import UTC, datetime

from ..database.config import Base

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False, 
        index=True
    )
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(UTC)
    )

    # author: Mapped[User] = relationship(back_populates='posts')