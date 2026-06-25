from sqlalchemy import String, select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sku: Mapped[str] = mapped_column(String(100), unique=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[int]
    currency: Mapped[str] = mapped_column(String(1), default="$")
    description: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id"))

    storage_relation = relationship("Storage", back_populates="product_relation")
    category_relation = relationship("Category", back_populates="product_relation")
    brand_relation = relationship("Brand", back_populates="product_relation")
    product_shopping_cart_relation = relationship("ProductShoppingCart", back_populates="product_relation")
    product_bill_relation = relationship("ProductBill", back_populates="product_relation")


    @classmethod
    def get_product(cls, session, name):
        stmt = select(cls).where(cls.name == name)
        product = session.scalar(stmt)
        return product


    @classmethod
    def get_product_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        product = session.scalar(stmt)
        return product


    @classmethod
    def insert_product(cls, session, name, price):
        product = cls(name = name, price = price)
        session.add(product)
        session.commit()
        return product
    

    @classmethod
    def update_product(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        product = session.scalar(stmt)

        if product is None:
            return None

        setattr(product, update_column, new_value)
        session.commit()
        return product


    @classmethod
    def delete_product(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        product = session.scalar(stmt)

        if product is None:
            return None

        session.delete(product)
        session.commit()
        return product