from sqlalchemy import ForeignKey, Date, String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from dateutil.relativedelta import relativedelta
from base import Base
from repositories.product import Product

class Bill(Base):
    __tablename__ = "bills"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_of_purchase: Mapped[datetime] = mapped_column(Date, default=lambda: datetime.now().date())
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product_amount: Mapped[int]
    bulk_total_price: Mapped[int]
    currency: Mapped[str] = mapped_column(String(1))

    user_relation = relationship("User", back_populates="bill_relation")
    product_relation = relationship("Product", back_populates="bill_relation")


    @classmethod
    def get_bill(cls, session, user_id):
        stmt = select(cls).where(cls.user_id == user_id)
        bill = session.scalars(stmt).all()
        return bill


    @classmethod
    def get_bill_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        bill = session.scalar(stmt)
        return bill


    @classmethod
    def insert_bill(cls, session, user_id, product_id, product_amount):
        product_price = session.get(Product, product_id).price
        bill = cls(user_id = user_id, product_id = product_id, product_amount = product_amount, bulk_total_price = product_price * product_amount, currency = "$")
        session.add(bill)
        session.commit()
        return bill


    @classmethod
    def update_bill(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        bill = session.scalar(stmt)

        if bill is None:
            return None

        setattr(bill, update_column, new_value)
        session.commit()
        return bill


    @classmethod
    def delete_bill(cls, session, id, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value).where(cls.user_id == id)
        bill = session.scalar(stmt)

        if bill is None:
            return None

        session.delete(bill)
        session.commit()
        return bill