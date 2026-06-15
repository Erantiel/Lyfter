from sqlalchemy import String, select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.exc import IntegrityError
from base import Base
from exceptions import DuplicateUsernameError

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    role_relation = relationship("Role", back_populates="user_relation")
    bill_relation = relationship("Bill", back_populates="user_relation")


    @classmethod
    def get_user_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        user = session.scalar(stmt)
        return user

    @classmethod
    def get_user_by_username(cls, session, username):
        stmt = select(cls).where(cls.username == username)
        user = session.scalar(stmt)
        return user


    @classmethod
    def insert_user(cls, session, username, password, role_id):
        try:
            existing_user = session.scalar(select(cls).where(cls.username == username))
            if existing_user:
                session.rollback()
                raise DuplicateUsernameError("Duplicate username. Username must be unique.")
            user = cls(username = username, password = password, role_id = role_id)
            session.add(user)
            session.commit()
            return user
        except IntegrityError:
            session.rollback()
            raise DuplicateUsernameError("Duplicate username. Username must be unique.")


    @classmethod
    def update_user(cls, session, filter_column, filter_value, update_column, new_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        user = session.scalar(stmt)

        if user is None:
            return None

        setattr(user, update_column, new_value)
        session.commit()
        return user


    @classmethod
    def delete_user(cls, session, filter_column, filter_value):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value)
        user = session.scalar(stmt)

        if user is None:
            return None

        session.delete(user)
        session.commit()
        return user