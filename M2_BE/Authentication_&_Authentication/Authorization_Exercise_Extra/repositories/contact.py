from sqlalchemy import String, select, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.exc import IntegrityError
from base import Base
from exceptions import DuplicatePhoneNumberError

class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))

    user_relation = relationship("User", back_populates="contact_relation")


    @classmethod
    def get_contact_by_id(cls, session, id):
        stmt = select(cls).where(cls.id == id)
        contact = session.scalar(stmt)
        return contact


    @classmethod
    def get_contacts_by_user_id(cls, session, user_id):
        stmt = select(cls).where(cls.user_id == user_id)
        contacts = session.scalars(stmt).all()
        return contacts
    

    @classmethod
    def get_contact_by_name(cls, session, name):
        stmt = select(cls).where(cls.name == name)
        contact = session.scalar(stmt)
        return contact


    @classmethod
    def insert_contact(cls, session, name, phone_number, email, user_id):
        try:
            existing_phone_number = session.scalar(select(cls).where(cls.phone_number == phone_number))
            if existing_phone_number:
                session.rollback()
                raise DuplicatePhoneNumberError("Duplicate phone number. Phone number must be unique.")
            contact = cls(name = name, phone_number = phone_number, email = email, user_id = user_id)
            session.add(contact)
            session.commit()
            return contact
        except IntegrityError:
            session.rollback()
            raise DuplicatePhoneNumberError("Duplicate phone number. Phone number must be unique.")


    @classmethod
    def update_contact(cls, session, filter_column, filter_value, update_column, new_value, user_id):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")

        if update_column not in allowed_filters:
            raise ValueError(f"Invalid update column: {update_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value).where(cls.user_id == user_id)
        contact = session.scalar(stmt)

        if contact is None:
            raise FileNotFoundError("Not such contact exist.")

        setattr(contact, update_column, new_value)
        session.commit()
        return contact


    @classmethod
    def delete_contact(cls, session, filter_column, filter_value, user_id):

        allowed_filters = cls.__table__.columns.keys()
        
        if filter_column not in allowed_filters:
            raise ValueError(f"Invalid filter column: {filter_column}")
        
        stmt = select(cls).where(getattr(cls, filter_column) == filter_value).where(cls.user_id == user_id)
        contact = session.scalar(stmt)

        if contact is None:
            raise FileNotFoundError("Not such contact exist.")

        session.delete(contact)
        session.commit()
        return contact