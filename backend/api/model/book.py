from api.model.db import db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from decimal import Decimal
from uuid import UUID


class Book(db.Model):
    __tablename__ = "book"

    id: Mapped[UUID] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    genre: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[Decimal] = mapped_column(nullable=True)
    date_published: Mapped[datetime] = mapped_column(nullable=False)
