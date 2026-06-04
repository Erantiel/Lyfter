from database import SqlAlchemyManager
from base import Base
from user import User
from address import Address
from vehicle import Vehicle
import fake_data

db = SqlAlchemyManager("postgresql", "postgres", "postgres", "localhost", "5432", "postgres")

Base.metadata.create_all(db.engine)

# users = [
#     User(name = "Marcelo"),
#     User(name = "Osias"),
#     User(name = "Carlos")
# ]

# addresses = [
#     Address(address = "2734 Hartway Street", user_id = 1),
#     Address(address = "3785 Blackwell", user_id = 2)
# ]

# vehicles = [
#     Vehicle(make = "Toyota", user_id = 1),
#     Vehicle(make = "Honda"),
#     Vehicle(make = "Mitsubichi", user_id = 1),
#     Vehicle(make = "Nissan", user_id = 3),
#     Vehicle(make = "Kia", user_id = 3),
#     Vehicle(make = "BYD")
# ]

# db.session.add_all(users)
# db.session.add_all(addresses)
# db.session.add_all(vehicles)
# db.session.commit()

# User.user_related_info(db.session, 2)
# Vehicle.all_vehicles_with_no_user(db.session)
# User.all_users_with_more_than_one_vehicle(db.session)
# Address.filter_address_by(db.session, "apt")
# fake_data.fake_user_with_address_and_vehicle_relation(db.session)

db.close_connection()