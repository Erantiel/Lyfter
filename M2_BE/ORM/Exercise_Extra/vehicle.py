from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import relationship, Mapped, mapped_column
from base import Base

class Vehicle(Base):
    __tablename__ = "vehicle"
    __table_args__ = {"schema":"orm"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    make: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("orm.user.id"), nullable=True)

    user = relationship("User", back_populates="vehicles")

    @classmethod
    def all_vehicles_with_no_user(cls, session):
        stmt = select(cls).where(cls.user_id.is_(None))
        vehicles = session.scalars(stmt).all()

        for vehicle in vehicles:
            print(vehicle.make)