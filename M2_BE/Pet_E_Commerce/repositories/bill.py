from sqlalchemy import ForeignKey, Date, String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from base import Base

class Bill(Base):
    __tablename__ = "bill"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    date_of_purchase: Mapped[datetime] = mapped_column(Date, default=lambda: datetime.now().date())
    final_price: Mapped[int]
    currency: Mapped[str] = mapped_column(String(1), default="$")

    user_relation = relationship("User", back_populates="bill_relation")
    product_bill_relation = relationship("ProductBill", back_populates="bill_relation")

    @classmethod
    def get_bills(cls, session):
        stmt = select(cls)
        bills = session.scalars(stmt).all()
        return bills

    @classmethod
    def get_bills_by_user_id(cls, session, user_id):
        stmt = select(cls).where(cls.user_id == user_id)
        bills = session.scalars(stmt).all()
        return bills


    @classmethod
    def get_bill_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        bill = session.scalar(stmt)
        return bill


    @classmethod
    def get_bill_by_user_id (cls, session, user_id):
        stmt = select(cls).where(cls.user_id == user_id)
        bill = session.scalar(stmt)
        return bill


    @classmethod
    def insert_bill(cls, session, user_id, final_price):
        bill = cls(user_id = user_id, final_price = final_price)
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
    def delete_bill(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        bill = session.scalar(stmt)

        if bill is None:
            return None

        session.delete(bill)
        session.commit()
        return bill