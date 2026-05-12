from database import PgManager
from flask import Flask, jsonify, request
from flask.views import MethodView
import validations

database = PgManager("localhost", 5432, "postgres", "postgres", "postgres", "-c search_path=lyfter_car_rental") #Database created and connection made


app = Flask(__name__)

database.backup_export_database("users.csv","lyfter_car_rental.users")
database.backup_export_database("vehicles.csv","lyfter_car_rental.vehicles")
database.backup_export_database("users_vehicles.csv","lyfter_car_rental.users_vehicles")


database.check_table_exists("users","lyfter_car_rental.users")
database.check_table_exists("vehicles","lyfter_car_rental.vehicles")
database.check_table_exists("rents","lyfter_car_rental.users_vehicles")


database.faker_users(200)
database.faker_vehicles(140)
database.faker_users_vehicles(50,150)


class Users(MethodView):
    def get(self):
        try:
            filter = request.args.get("filter")
            value = request.args.get("value")
            allowed_filters = ["id", "name", "email", "username", "password", "birthday", "overdue", "status"]
            
            if not filter:
                get_query = database.execute_query("""
                SELECT * FROM users
                ORDER BY id ASC
                """)
                return jsonify({"response":get_query}), 200
            
            if filter not in allowed_filters:
                return jsonify({"error":"This method only accepts id, name, email, username, password, birthday, overdue or status."}), 404
            
            filter_query = database.execute_query(f"""
            SELECT * FROM users
            WHERE {filter} = %s
            """,(value,))
            
            database.close_connection
            return jsonify({"response":filter_query}), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400



    def post(self):
        try:
            data = request.json
            validations.validate_keys_users(data)
            validations.validate_data_users(data)
            
            database.execute_query("""
            INSERT INTO users(name, email, username, password, birthday)
            VALUES (%s, %s, %s, %s, %s)
            """,(data['name'], data['email'], data['username'], data['password'], data['birthday']))
            
            database.close_connection
            return jsonify({"response":"User added."}), 201
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def put(self):
        try:
            update = request.args.get("update")
            filter = request.args.get("filter")
            value = request.args.get("value")
            data = request.json
            
            if not update or not filter or not value:
                return jsonify({"error":"In order to update the table, the following parameters are needed: update, filter and value."}), 400
            
            database.execute_query(f"""
            UPDATE users 
            SET {update} = %s
            WHERE {filter} = %s
            """,(data[update], value))
            
            database.close_connection
            return jsonify({"response":"Database updated."}), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


class Vehicles(MethodView):
    def get(self):
        try:
            filter = request.args.get("filter")
            value = request.args.get("value")
            allowed_filters = ["id", "make", "model", "manufacture_year", "status"]
            
            if not filter:
                get_query = database.execute_query(f"""
                SELECT * FROM vehicles
                ORDER BY id ASC
                """)
                return jsonify({"response":get_query}), 200
            
            if filter not in allowed_filters:
                return jsonify({"error":"This method only accepts id, make, model, manufacture_year or status."}), 404
            
            filter_query = database.execute_query(f"""
            SELECT * FROM vehicles
            WHERE {filter} = %s
            """,(value,))
            
            database.close_connection
            return jsonify({"response":filter_query}), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400



    def post(self):
        try:
            data = request.json
            validations.validate_keys_vehicles(data)
            validations.validate_data_vehicles(data)
            
            database.execute_query("""
            INSERT INTO vehicles(make, model, manufacture_year)
            VALUES (%s, %s, %s)""",(data['make'], data['model'], data['manufacture_year']))
            
            database.close_connection
            return jsonify({"response":"Vehicle added."}), 201
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def put(self):
        try:
            update = request.args.get("update")
            filter = request.args.get("filter")
            value = request.args.get("value")
            data = request.json
            
            if not update or not filter or not value:
                return jsonify({"error":"In order to update the table, the following parameters are needed: update, filter and value."}), 400
            
            database.execute_query(f"""
            UPDATE vehicles 
            SET {update} = %s
            WHERE {filter} = %s
            """,(data[update], value))
            
            database.close_connection
            return jsonify({"response":"Database updated."}), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


class UsersVehicles(MethodView):
    def get(self):
        try:
            filter = request.args.get("filter")
            value = request.args.get("value")
            allowed_filters = ["id", "user_id", "vehicle_id", "rent_date", "rent_end_date", "rent_devolution_date", "status"]
            
            if not filter:
                get_query = database.execute_query(f"""
                SELECT * FROM users_vehicles
                ORDER BY id ASC
                """)
                return jsonify({"response":get_query}), 200
            
            if filter not in allowed_filters:
                return jsonify({"error":"This method only accepts id, user_id, vehicle id, rent_date, rent_end_date, rent_devolution_date and status."}), 404
            
            filter_query = database.execute_query(f"""
            SELECT * FROM users_vehicles
            WHERE {filter} = &s
            """,(value,))
            
            database.close_connection
            return jsonify({"response":filter_query}), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400



    def post(self):
        try:
            data = request.json
            validations.validate_keys_users_vehicles(data)
            validations.validate_data_users_vehicles(data)
            
            car_status_query = database.execute_query(f"""
            SELECT status FROM vehicles
            WHERE id = %s
            """,(data['vehicle_id']))
            
            user_status_query = database.execute_query(f"""
            SELECT status FROM users
            WHERE id = %s
            """,(data['user_id']))

            user_overdue_query = database.execute_query(f"""
            SELECT overdue FROM users
            WHERE id = %s
            """,(data['user_id']))
            
            car_status = car_status_query[0][0]
            user_status = user_status_query[0][0]
            user_overdue = user_overdue_query[0][0]

            if car_status == 'rented':
                return jsonify({"error":"The vehicle you are trying to rent is already rented by an user."}), 400
            elif car_status == 'not available':
                return jsonify({"error":"The vehicle you are trying to rent is not available."}), 400
            elif user_status != 'active':
                return jsonify({"error":"The user you are trying to use is not available or up to date to be used."}), 400
            elif user_overdue == True:
                return jsonify({"error":"The user you are trying to use is overdue. Rents are not possible on overdue users."}), 400
            
            database.execute_query("""
            INSERT INTO users_vehicles(user_id, vehicle_id)
            VALUES (%s, %s)""",(data['user_id'], data['vehicle_id']))
            
            database.execute_query(f"""
            UPDATE vehicles
            SET status = 'rented'
            WHERE id = %s
            """,(data['vehicle_id']))

            database.close_connection
            return jsonify({"response":"Rent added."}), 201
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def put(self):
        try:
            update = request.args.get("update")
            filter = request.args.get("filter")
            value = request.args.get("value")
            data = request.json
            
            if not update or not filter or not value:
                return jsonify({"error":"In order to update the table, the following parameters are needed: update, filter and value."}), 400
            
            query_update_status = database.execute_query(f"""
            UPDATE users_vehicles 
            SET {update} = %s
            WHERE {filter} = %s
            """, (data[update], value))

            query_select_id = database.execute_query(f"""
            SELECT id FROM users_vehicles
            WHERE {filter} = %s
            """, (value,))

            query_select_vehicle_id = database.execute_query(f"""
            SELECT vehicle_id FROM users_vehicles
            WHERE {filter} = %s
            """, (value,))

            user_vehicle_id = query_select_id[0][0]
            vehicle_id = query_select_vehicle_id[0][0]
            
            if data[update] == "completed":
                query_rent_completed = database.execute_query(f"""
                UPDATE vehicles
                SET status = 'available'
                WHERE id = {vehicle_id}
                """, (value,))
                
                query_date_completion = database.execute_query(f"""
                UPDATE users_vehicles
                SET rent_devolution_date = CURRENT_DATE
                WHERE id = {user_vehicle_id}
                """, (value,))
            
            database.close_connection
            return jsonify({"response":"Database updated."}), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


users_view = Users.as_view("users_api")
vehicles_view = Vehicles.as_view("vehicles_api")
users_vehicles_view = UsersVehicles.as_view("user_vehicles_api")

app.add_url_rule("/users", methods=["GET", "POST", "PUT"], view_func=users_view)
app.add_url_rule("/vehicles", methods=["GET", "POST", "PUT"], view_func=vehicles_view)
app.add_url_rule("/users_vehicles", methods=["GET", "POST", "PUT"], view_func=users_vehicles_view)

if __name__ == "__main__":
    app.run(host="localhost", debug=True, use_reloader=False)