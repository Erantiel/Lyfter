from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from base import Base

class Vehicle(Base):
    __tablename__ = "vehicle"
    __table_args__ = {"schema":"orm"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    make: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("orm.user.id"), nullable=True)

    user = relationship("User", back_populates="vehicles")