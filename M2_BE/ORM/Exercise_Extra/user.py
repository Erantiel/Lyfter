from sqlalchemy import String, select, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from base import Base
from vehicle import Vehicle
from address import Address
from faker import Faker
from faker_vehicle import VehicleProvider
import random
class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema":"orm"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

    address = relationship("Address", back_populates="user")
    vehicles = relationship("Vehicle", back_populates="user")


    @classmethod
    def all_users_with_more_than_one_vehicle(cls, session):
        stmt = select(cls).join(cls.vehicles).group_by(cls.id).having(func.count(Vehicle.id)>1)
        users = session.scalars(stmt).all()

        for user in users:
            print(f"{user.name} has {len(user.vehicles)} vehicles.")


    @classmethod
    def user_related_info(cls, session, user_id):
        cls = session.get(cls, user_id)

        if not cls:
            return print("User not found.")
        
        print(f"User: {cls.name}")

        for address in cls.address:
            print(f"Address: {address.address}")
        
        for position, vehicle in enumerate(cls.vehicles):
            print(f"Vehicle {position + 1}: {vehicle.make}")


    @classmethod
    def fake_data(cls, session):
        fake = Faker()
        fake.add_provider(VehicleProvider)

        for _ in range(20):
            user = cls(name = fake.first_name())
            session.add(user)
        session.commit()
        
        user_ids = session.scalars(select(cls.id)).all()
        random.shuffle(user_ids)
        none_user_ids = random.sample(range(20),5)
        
        for user_id in user_ids:
            existing = session.scalar(select(Address).where(Address.user_id == user_id))
            if existing:
                continue
            address = Address(address = fake.address(), user_id = user_id)
            session.add(address)
        
        for r in range (20):
            if r in none_user_ids:
                user_id = None
            else:
                user_id = random.choice(user_ids)
            vehicle = Vehicle(make = fake.vehicle_make(), user_id = user_id)
            session.add(vehicle)

        session.commit()