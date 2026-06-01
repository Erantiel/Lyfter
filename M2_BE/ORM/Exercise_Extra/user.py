from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from base import Base

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema":"orm"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

    addresses = relationship("Address", back_populates="user")
    vehicles = relationship("Vehicle", back_populates="user")