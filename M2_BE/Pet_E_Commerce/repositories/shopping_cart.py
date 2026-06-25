from sqlalchemy import select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user_relation = relationship("User", back_populates="shopping_cart_relation")
    product_shopping_cart_relation = relationship("ProductShoppingCart", back_populates="shopping_cart_relation")


    @classmethod
    def get_shopping_cart_by_user_id(cls, session, user_id):
        stmt = select(cls).where(cls.user_id == user_id)
        shopping_cart = session.scalar(stmt)
        return shopping_cart


    @classmethod
    def get_shopping_cart_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        shopping_cart = session.scalar(stmt)
        return shopping_cart


    @classmethod
    def insert_shopping_cart(cls, session, user_id):
        shopping_cart = cls(user_id = user_id)
        session.add(shopping_cart)
        session.commit()
        return shopping_cart
    

    @classmethod
    def update_shopping_cart(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        shopping_cart = session.scalar(stmt)

        if shopping_cart is None:
            return None

        setattr(shopping_cart, update_column, new_value)
        session.commit()
        return shopping_cart


    @classmethod
    def delete_shopping_cart(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        shopping_cart = session.scalar(stmt)

        if shopping_cart is None:
            return None

        session.delete(shopping_cart)
        session.commit()
        return shopping_cart