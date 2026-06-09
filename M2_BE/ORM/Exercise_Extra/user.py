from sqlalchemy import String, select, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from base import Base
from vehicle import Vehicle

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema":"orm"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

    address = relationship("Address", back_populates="user", uselist=False)
    vehicles = relationship("Vehicle", back_populates="user")


    @classmethod
    def all_users_with_more_than_one_vehicle(cls, session):
        stmt = select(cls).join(cls.vehicles).group_by(cls.id).having(func.count(Vehicle.id)>1)
        users = session.scalars(stmt).all()

        for user in users:
            print(f"{user.name} has {len(user.vehicles)} vehicles.")


    @classmethod
    def user_related_info(cls, session, user_id):
        user = session.get(cls, user_id)

        if not user:
            return print("User not found.")
        
        print(f"User: {user.name}")

        if user.address:
            print(f"Address: {user.address.address}")
        
        for position, vehicle in enumerate(user.vehicles):
            print(f"Vehicle {position + 1}: {vehicle.make}")