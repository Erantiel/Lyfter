from user import User
from vehicle import Vehicle
from address import Address
from sqlalchemy import select, func
from faker import Faker
from faker_vehicle import VehicleProvider
import random

def all_vehicles_with_no_user(session):
    stmt = select(Vehicle).where(Vehicle.user_id.is_(None))
    vehicles = session.scalars(stmt).all()

    for vehicle in vehicles:
        print(vehicle.make)


def all_users_with_more_than_one_car(session):
    stmt = select(User).join(Vehicle).group_by(User.id).having(func.count(Vehicle.id)>1)
    users = session.scalars(stmt).all()

    for user in users:
        print(f"{user.name} has {len(user.vehicles)} vehicles.")


def all_addresses_with_steet(session):
    stmt = select(Address).where(Address.address.contains("Street"))
    addresses = session.scalars(stmt).all()

    if not addresses:
        return print("No addresses with 'Street' found.")

    for address in addresses:
        print(address.address)


def user_related_info(session, user_id):
    user = session.get(User, user_id)

    if not user:
        return print("User not found.")
    
    print(f"User: {user.name}")

    for address in user.addresses:
        print(f"Address: {address.address}")
    
    for position, vehicle in enumerate(user.vehicles):
        print(f"Vehicle {position + 1}: {vehicle.make}")


def fake_data(session):
    fake = Faker()
    fake.add_provider(VehicleProvider)

    for _ in range(20):
        user = User(name = fake.first_name())
        session.add(user)
    session.commit()
    user_ids = session.scalars(select(User.id)).all()
    random.shuffle(user_ids)
    
    for user_id in user_ids:
        existing = session.scalar(select(Address).where(Address.user_id == user_id))
        if existing:
            continue
        address = Address(address = fake.address(), user_id = user_id)
        session.add(address)
    
    for _ in range (20):
        vehicles = Vehicle(make = fake.vehicle_make(), user_id = random.choice(user_ids + [None]))
        session.add(vehicles)

    session.commit()