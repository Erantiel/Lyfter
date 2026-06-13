from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base
from exceptions import DuplicateRoleError

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    role: Mapped[str] = mapped_column(String(25))

    user_relation = relationship("User", back_populates="role_relation")


    @classmethod
    def get_role(cls, session, role):
        stmt = select(cls).where(cls.role == role)
        role = session.scalar(stmt)
        return role


    @classmethod
    def get_role_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        role = session.scalar(stmt)
        return role


    @classmethod
    def insert_role(cls, session, role):
        existing_role = session.scalar(select(cls).where(cls.role == role))
        if existing_role:
            raise DuplicateRoleError("Duplicate role.")
        role = cls(role = role)
        session.add(role)
        session.commit()
        return role


    @classmethod
    def update_role(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        role = session.scalar(stmt)

        if role is None:
            return None

        setattr(role, update_column, new_value)
        session.commit()
        return role


    @classmethod
    def delete_role(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        role = session.scalar(stmt)

        if role is None:
            return None

        session.delete(role)
        session.commit()
        return role