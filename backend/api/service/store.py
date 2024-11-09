from api.model.item import Item
from api.model.order import Order
from api.model.item_order import ItemOrder

from tracing.log import logger
from api.model.db import db
from sqlalchemy import insert, update, select
from typing import Dict
from flask import abort
from decimal import Decimal
from datetime import datetime


class StoreService:
    def get_items(self):
        logger.info("Retrieving items from DB")
        return Item.query.where(Item.is_available == True).all()

    def get_item(self, item_id):
        logger.info(f"Retrieving item with id {item_id} from DB")
        return Item.query.get_or_404(item_id)

    def get_all_orders(self):
        logger.info("Retrieving orders from DB")
        return Order.query.all()

    def get_orders_by_user_id(self, user_id):
        logger.info(f"Retrieving orders from DB for userId={user_id}")
        return Order.query.where(Order.user_id == user_id).all()

    def add_items(self, items):
        logger.info("Inserting new items into DB")
        new_items = [Item(**item) for item in items]
        db.session.add_all(new_items)
        db.session.commit()

    def add_item(self, item):
        logger.info("Inserting new item into DB")
        db.session.add(Item(**item))
        db.session.commit()

    def update_item(self, item_id, item_update):
        logger.info(f"Updating item with id {item_id}")
        Item.query.get_or_404(item_id)
        item_update["date_updated"] = datetime.now()
        update_stmt = update(Item).where(Item.id == item_id).values(
            item_update)
        db.session.execute(update_stmt)
        db.session.commit()

    def delete_item(self, item_id):
        logger.info(f"Soft deleting item with id {item_id}")
        item: Dict[str, any] | None = Item.query.get_or_404(item_id)
        item.date_updated = datetime.now()
        item.is_available = False
        db.session.commit()

    def purchase_specific_item(self, user_id, item_id, count):
        logger.info("Purchasing a specific item")
        order = Order(user_id=user_id)
        db.session.add(order)
        db.session.flush()
        order_price = self.create_item_order(order.id, item_id, count, )
        order.order_price = order_price
        db.session.commit()
        return f"Item has been bought at a total price of ${order_price}"

    def create_item_order(self, order_id, item_id, count):
        item: Item = Item.query.get(item_id)
        if item is None:
            db.session.rollback()
            abort(404, description="Item does not exist")
        total_price = float(item.price * count)
        new_count = item.count - count
        if new_count < 0:
            logger.info("There's not enough inventory for that item")
            abort(
                400,
                description="There's not enough inventory of the given item")
        item.count = new_count
        item.date_updated = datetime.now()
        db.session.flush()
        item_order = ItemOrder(order_id=order_id,
                               item_id=item_id,
                               amount_bought=count,
                               total_price=total_price)
        db.session.add(item_order)
        return total_price

    def purchase_items(self, user_id, items_info):
        logger.info("Purchasing items")
        order = Order(user_id=user_id)
        db.session.add(order)
        db.session.flush()
        order_price = 0
        for item_info in items_info:
            item_id = item_info["id"]
            count = item_info["count"]
            order_price += self.create_item_order(order.id, item_id, count)
        order.order_price = order_price
        db.session.commit()
        return f"Items have been bought; total price = {order_price}"


store_service = StoreService()
