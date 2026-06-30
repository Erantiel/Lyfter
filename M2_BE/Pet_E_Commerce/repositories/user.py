from sqlalchemy import String, select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base
from exceptions import UniqueDataError

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped [str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str]
    email: Mapped [str] = mapped_column(String(100), unique=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))
    refresh_token: Mapped[str] = mapped_column(nullable=True, default=None)

    role_relation = relationship("Role", back_populates="user_relation")
    bill_relation = relationship("Bill", back_populates="user_relation")
    shopping_cart_relation = relationship("ShoppingCart", back_populates="user_relation")


    @classmethod
    def get_user_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        user = session.scalar(stmt)
        return user


    @classmethod
    def get_user_by_name(cls, session, name):
        stmt = select(cls).where(cls.name == name)
        user = session.scalar(stmt)
        return user


    @classmethod
    def get_users(cls, session):
        stmt = select(cls)
        user = session.scalars(stmt).all()
        return user


    @classmethod
    def login_user(cls, session, username, password):
        stmt = select(cls).where(cls.username == username, cls.password == password)
        user = session.scalar(stmt)
        return user


    @classmethod
    def insert_user(cls, session, name, username, password, email, role_id):
        username = session.scalar(select(cls).where(cls.username == username))
        email = session.scalar(select(cls).where(cls.email == email))
        if username:
            session.rollback()
            raise UniqueDataError("Already existing username. Username must be unique.")
        if email:
            session.rollback()
            raise UniqueDataError("Already existing email. Email must be unique.")
        user = cls(name = name, username = username, password = password, email = email, role_id = role_id)
        session.add(user)
        session.commit()
        return user


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