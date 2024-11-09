from api.model.db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import FetchedValue
from decimal import Decimal
from datetime import datetime
from uuid import UUID


class Order(db.Model):
    __tablename__ = "order"

    id: Mapped[UUID] = mapped_column(primary_key=True,
                                     nullable=False,
                                     server_default=FetchedValue())
    user_id: Mapped[str] = mapped_column(nullable=False)
    order_price: Mapped[Decimal] = mapped_column(nullable=True)
    date_created: Mapped[datetime] = mapped_column(
        nullable=False,
        server_default=FetchedValue())
    item_orders = relationship("ItemOrder", back_populates="order")
