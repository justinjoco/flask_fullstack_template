from api.model.db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal
from sqlalchemy import ForeignKey
from uuid import UUID
from sqlalchemy.schema import FetchedValue


class ItemOrder(db.Model):
    __tablename__ = "item_order"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    order_id: Mapped[str] = mapped_column(ForeignKey("order.id"),
                                          nullable=False)
    item_id: Mapped[str] = mapped_column(ForeignKey("item.id"), nullable=False)
    amount_bought: Mapped[int] = mapped_column(nullable=False)
    total_price: Mapped[Decimal] = mapped_column(nullable=False)
    date_created: Mapped[datetime] = mapped_column(
        nullable=False,
        server_default=FetchedValue())
    order = relationship("Order", back_populates="item_orders")
    item = relationship("Item", back_populates="item_orders")
