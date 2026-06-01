from database import SqlAlchemyManager
from user import User
from address import Address
from vehicle import Vehicle

db = SqlAlchemyManager("postgresql", "postgres", "postgres", "localhost", "5432", "postgres")


# Class creations
user = User(db.session, db.metadata_obj, db.engine)
address = Address(db.session, db.metadata_obj, db.engine)
vehicle = Vehicle(db.session, db.metadata_obj, db.engine)


# INSERTS --------------------------
# user.insert_user("Marcelo") #id = 1
# user.insert_user("Osias") #id = 2
# user.insert_user("Carlos") #id = 3

# address.insert_address("2734 Hartway Street",1)
# address.insert_address("3785 Blackwell",2)

# vehicle.insert_vehicle("Toyota",1)
# vehicle.insert_vehicle("Honda")
# vehicle.insert_vehicle("Mitsubichi",1)
# vehicle.insert_vehicle("Nissan",3)
# vehicle.insert_vehicle("Kia",3)


# UPDATES --------------------------
# user.update_user("id", 1, "name", "Marco")
# user.update_user("name", "Osias", "name", "Luis")

# address.update_address("user_id", 1, "address", "2229 Hannah Street")
# address.update_address("id", 2, "address", "3499 Parker Drive")

# vehicle.update_vehicle("id", 1, "make", "Mazda")
# vehicle.update_vehicle("make", "Honda", "make", "Subaru")
# vehicle.associate_vehicle_user("id", 2, 2)


# DELETES --------------------------
# vehicle.delete_vehicle("id", 2)

# address.delete_address("id", 2)

# user.delete_user("id", 2)


# SELECt --------------------------
# print(user.select_user())
# print(address.select_address())
# print(vehicle.select_vehicle())
# print(vehicle.select_all_vehicle_with_no_user())
# print(user.select_users_with_more_than_one_vehicle(vehicle))
print(address.select_address_with_street())

db.close_connection()