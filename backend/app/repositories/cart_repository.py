from typing import Optional
from sqlalchemy.orm import Session, joinedload
from app.models.cart import Cart, CartItem
from app.models.course import Course


class CartRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_or_create_user_cart(self, user_id: int) -> Cart:
        cart = (
            self.db.query(Cart)
            .filter(Cart.user_id == user_id)
            .options(joinedload(Cart.items).joinedload(CartItem.course).joinedload(Course.instructor))
            .first()
        )
        if not cart:
            cart = Cart(user_id=user_id)
            self.db.add(cart)
            self.db.commit()
            self.db.refresh(cart)
        return cart

    def add_course_to_cart(self, cart_id: int, course_id: int) -> CartItem:
        existing = self.db.query(CartItem).filter(CartItem.cart_id == cart_id, CartItem.course_id == course_id).first()
        if existing:
            return existing
        item = CartItem(cart_id=cart_id, course_id=course_id)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def remove_item(self, cart_id: int, course_id: int) -> bool:
        item = self.db.query(CartItem).filter(CartItem.cart_id == cart_id, CartItem.course_id == course_id).first()
        if item:
            self.db.delete(item)
            self.db.commit()
            return True
        return False

    def clear_cart(self, cart_id: int) -> None:
        self.db.query(CartItem).filter(CartItem.cart_id == cart_id).delete()
        self.db.commit()
