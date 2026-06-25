from sqlalchemy import select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class ProductShoppingCart(Base):
    __tablename__ = "product_shopping_cart"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    shopping_cart_id: Mapped[int] = mapped_column(ForeignKey("shopping_cart.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product_amount: Mapped[int]

    shopping_cart_relation = relationship("ShoppingCart", back_populates="product_shopping_cart_relation")
    product_relation = relationship("Product", back_populates="product_shopping_cart_relation")


    @classmethod
    def get_product_shopping_cart_by_shopping_cart_id(cls, session, shopping_cart_id):
        stmt = select(cls).where(cls.shopping_cart_id == shopping_cart_id)
        product_shopping_cart = session.scalar(stmt)
        return product_shopping_cart


    @classmethod
    def get_product_shopping_cart_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        product_shopping_cart = session.scalar(stmt)
        return product_shopping_cart


    @classmethod
    def insert_product_shopping_cart(cls, session, shopping_cart_id, product_id, product_amount):
        product_shopping_cart = cls(shopping_cart_id = shopping_cart_id, product_id = product_id, product_amount = product_amount)
        session.add(product_shopping_cart)
        session.commit()
        return product_shopping_cart
    

    @classmethod
    def update_product_shopping_cart(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        product_shopping_cart = session.scalar(stmt)

        if product_shopping_cart is None:
            return None

        setattr(product_shopping_cart, update_column, new_value)
        session.commit()
        return product_shopping_cart


    @classmethod
    def delete_product_shopping_cart(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        product_shopping_cart = session.scalar(stmt)

        if product_shopping_cart is None:
            return None

        session.delete(product_shopping_cart)
        session.commit()
        return product_shopping_cart