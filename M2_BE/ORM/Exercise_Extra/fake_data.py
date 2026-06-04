import random
from faker import Faker
from faker_vehicle import VehicleProvider
from address import Address
from sqlalchemy import select
from vehicle import Vehicle
from  user import User

def fake_user_with_address_and_vehicle_relation(session):
    fake = Faker()
    fake.add_provider(VehicleProvider)

    for _ in range(20):
        user = User(name = fake.first_name())
        session.add(user)
    session.commit()
    
    user_ids = session.scalars(select(User.id)).all()
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