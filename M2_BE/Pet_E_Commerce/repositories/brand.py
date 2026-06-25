from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class Brand(Base):
    __tablename__ = "brand"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    product_relation = relationship("Product", back_populates="brand_relation")


    @classmethod
    def get_brand_by_name(cls, session, name):
        stmt = select(cls).where(cls.name == name)
        brand = session.scalar(stmt)
        return brand


    @classmethod
    def get_brand_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        brand = session.scalar(stmt)
        return brand


    @classmethod
    def insert_brand(cls, session, name):
        brand = cls(name = name)
        session.add(brand)
        session.commit()
        return brand
    

    @classmethod
    def update_brand(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        brand = session.scalar(stmt)

        if brand is None:
            return None

        setattr(brand, update_column, new_value)
        session.commit()
        return brand


    @classmethod
    def delete_brand(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        brand = session.scalar(stmt)

        if brand is None:
            return None

        session.delete(brand)
        session.commit()
        return brand