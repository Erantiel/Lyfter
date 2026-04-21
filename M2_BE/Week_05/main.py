from database import PgManager
import files


database = PgManager("localhost", 5432, "postgres", "postgres", "postgres", "-c search_path=lyfter_car_rental") #Database created and connection made


database.execute_query( #Create table on PgAdmin 4 for users
    """CREATE TABLE users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        birthday TEXT NOT NULL,
        status VARCHAR(50) NOT NULL
        );"""
)


database.execute_query( #Create table on PgAdmin 4 for vehicles
    """CREATE TABLE vehicles(
        id SERIAL PRIMARY KEY,
        make VARCHAR(50) NOT NULL,
        model VARCHAR(50) NOT NULL,
        manufacture_year TEXT NOT NULL,
        status VARCHAR(50) NOT NULL
        );"""
)


database.execute_query( #Create table on PgAdmin 4 for users_vehicles
    """CREATE TABLE users_vehicles(
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        vehicle_id INT NOT NULL,
        rent_date DATE DEFAULT CURRENT_DATE,
        rent_status VARCHAR(50) NOT NULL
        );"""
)


user_list = files.open_json("users_data_generated.json") #Retrieves the list with dicionaries from the file users_data_generated.json
vehicle_list = files.open_json("vehicles_data_generated.json") #Retrieves the list with dicionaries from the file vehicles_data_generated.json


for user in user_list: #Inserts into the table "users" all the information of user_list in PgAdmin 4
        database.execute_query("""
        INSERT INTO users(name, email, username, password, birthday, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        user['name'],
        user['email'],
        user['username'],
        user['password'],
        user['birthday'],
        user['status']
    ))


for vehicle in vehicle_list: #Inserts into the table "vehicles" all the information of vehicle_list in PgAdmin 4
        database.execute_query("""
        INSERT INTO vehicles(make, model, manufacture_year, status)
        VALUES (%s, %s, %s, %s)
    """, (
        vehicle['make'],
        vehicle['model'],
        vehicle['manufacture_year'],
        vehicle['status']
    ))


# database.execute_query(""" #Test to see if DATE DEFAULT CURRENT_DATE is working (it is)
#         INSERT INTO users_vehicles(user_id, vehicle_id, rent_status)
#         VALUES (%s, %s, %s)
#     """, (
#         1,
#         1,
#         "rented"
#     ))


database.close_connection() #Closes connection and cursor