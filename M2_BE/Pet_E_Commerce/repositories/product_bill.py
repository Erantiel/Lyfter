from sqlalchemy import select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base
from repositories.product import Product

class ProductBill(Base):
    __tablename__ = "product_bill"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    bill_id: Mapped[int] = mapped_column(ForeignKey("bill.id"))
    product_amount: Mapped[int]
    total_amount: Mapped[int]
    currency: Mapped[str] = mapped_column(default="$")

    product_relation = relationship("Product", back_populates="product_bill_relation")
    bill_relation = relationship("Bill", back_populates="product_bill_relation")


    @classmethod
    def get_product_bill_by_bill_id(cls, session, bill_id):
        stmt = select(cls).where(cls.bill_id == bill_id)
        product_bill = session.scalar(stmt)
        return product_bill


    @classmethod
    def get_product_bill_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        product_bill = session.scalar(stmt)
        return product_bill


    @classmethod
    def insert_product_bill(cls, session, product_id, bill_id, product_amount, total_amount):
        product_price = session.get(Product, product_id).price
        product_bill = cls(product_id = product_id, bill_id = bill_id, product_amount = product_amount, total_amount = product_price * product_amount)
        session.add(product_bill)
        session.commit()
        return product_bill
    

    @classmethod
    def update_product_bill(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        product_bill = session.scalar(stmt)

        if product_bill is None:
            return None

        setattr(product_bill, update_column, new_value)
        session.commit()
        return product_bill


    @classmethod
    def delete_product_bill(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        product_bill = session.scalar(stmt)

        if product_bill is None:
            return None

        session.delete(product_bill)
        session.commit()
        return product_bill