from database import SqlAlchemyManager
from base import Base
from user import User
from address import Address
from vehicle import Vehicle
import functions

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

# functions.user_related_info(db.session, 1)
# functions.all_vehicles_with_no_user(db.session)
# functions.all_users_with_more_than_one_car(db.session)
# functions.all_addresses_with_steet(db.session)
# functions.fake_data(db.session)

db.close_connection()