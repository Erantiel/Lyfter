from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from base import Base

class Address(Base):
    __tablename__ = "address"
    __table_args__ = {"schema":"orm"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("orm.user.id"), unique=True)

    user = relationship("User", back_populates="addresses")