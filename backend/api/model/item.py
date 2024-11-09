from api.model.db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from sqlalchemy.schema import FetchedValue


class Item(db.Model):
    __tablename__ = "item"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[Decimal] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(nullable=False)
    is_available: Mapped[bool] = mapped_column(nullable=False,
                                               server_default=FetchedValue())
    date_created: Mapped[datetime] = mapped_column(
        nullable=False,
        server_default=FetchedValue())
    date_updated: Mapped[datetime] = mapped_column(
        nullable=False,
        server_default=FetchedValue())
    item_orders = relationship("ItemOrder", back_populates="item")
