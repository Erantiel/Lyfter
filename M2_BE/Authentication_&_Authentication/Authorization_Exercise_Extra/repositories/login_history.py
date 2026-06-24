from sqlalchemy import select, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from base import Base


class LoginHistory(Base):
    __tablename__ = "login_history"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now())
    ip_address: Mapped[str]
    login_status: Mapped[str]

    user_relation = relationship("User", back_populates="login_history_relation")


    @classmethod
    def get_login_hisory_by_user_id(cls, session, user_id):
        stmt = select(cls).where(cls.user_id == user_id)
        login_history = session.scalars(stmt).all()
        return login_history


    @classmethod
    def get_login_hisory(cls, session):
        stmt = select(cls)
        login_history = session.scalars(stmt).all()
        return login_history


    @classmethod
    def insert_login(cls, session, user_id, ip_address, login_status):
        login_history = cls(user_id = user_id, ip_address = ip_address, login_status = login_status)
        session.add(login_history)
        session.commit()
        return login_history