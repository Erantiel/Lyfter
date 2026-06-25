from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str]

    product_relation = relationship("Product", back_populates="category_relation")


    @classmethod
    def get_category_by_name(cls, session, name):
        stmt = select(cls).where(cls.name == name)
        category = session.scalar(stmt)
        return category


    @classmethod
    def get_category_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        category = session.scalar(stmt)
        return category


    @classmethod
    def insert_category(cls, session, name, description):
        category = cls(name = name, description = description)
        session.add(category)
        session.commit()
        return category
    

    @classmethod
    def update_category(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        category = session.scalar(stmt)

        if category is None:
            return None

        setattr(category, update_column, new_value)
        session.commit()
        return category


    @classmethod
    def delete_category(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        category = session.scalar(stmt)

        if category is None:
            return None

        session.delete(category)
        session.commit()
        return category