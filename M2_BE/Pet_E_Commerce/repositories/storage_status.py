from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class StorageStatus(Base):
    __tablename__ = "storage_status"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

    storage_relation = relationship("Storage", back_populates="storage_status_relation")


    @classmethod
    def get_storage_status_by_name(cls, session, name):
        stmt = select(cls).where(cls.name == name)
        storage_status = session.scalar(stmt)
        return storage_status


    @classmethod
    def get_storage_status_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        storage_status = session.scalar(stmt)
        return storage_status


    @classmethod
    def get_storage_statuses(cls, session):
        stmt = select(cls)
        storage_status = session.scalars(stmt).all()
        return storage_status


    @classmethod
    def insert_storage_status(cls, session, name):
        storage_status = cls(name = name)
        session.add(storage_status)
        session.commit()
        return storage_status
    

    @classmethod
    def update_storage_status(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        storage_status = session.scalar(stmt)

        if storage_status is None:
            return None

        setattr(storage_status, update_column, new_value)
        session.commit()
        return storage_status


    @classmethod
    def delete_storage_status(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        storage_status = session.scalar(stmt)

        if storage_status is None:
            return None

        session.delete(storage_status)
        session.commit()
        return storage_status