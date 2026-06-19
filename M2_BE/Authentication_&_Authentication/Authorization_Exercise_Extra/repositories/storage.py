from sqlalchemy import ForeignKey, Date, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from dateutil.relativedelta import relativedelta
from base import Base

class Storage(Base):
    __tablename__ = "storage"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    amount: Mapped[int]
    date_of_admission: Mapped[datetime] = mapped_column(Date, default=lambda: datetime.now().date())
    expiration_date: Mapped[datetime] = mapped_column(Date, default=lambda: datetime.now().date() + relativedelta(months=1))

    product_relation = relationship("Product", back_populates="storage_relation")


    @classmethod
    def get_storage_by_product_id(cls, session, product_id):
        stmt = select(cls).where(cls.product_id == product_id)
        storage = session.scalar(stmt)
        return storage


    @classmethod
    def get_storage_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        storage = session.scalar(stmt)
        return storage


    @classmethod
    def get_storage(cls, session):
        stmt = select(cls)
        storage = session.scalars(stmt).all()
        return storage


    @classmethod
    def insert_storage(cls, session, product_id, amount):
        storage = cls(product_id = product_id, amount = amount)
        session.add(storage)
        session.commit()
        return storage


    @classmethod
    def update_storage(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        storage = session.scalar(stmt)

        if storage is None:
            return None

        setattr(storage, update_column, new_value)
        session.commit()
        return storage


    @classmethod
    def delete_storage(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        storage = session.scalar(stmt)

        if storage is None:
            return None

        session.delete(storage)
        session.commit()
        return storage