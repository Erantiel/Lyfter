from database import PgManager
from flask import Flask, jsonify, request
from flask.views import MethodView
import validations

database = PgManager("localhost", 5432, "postgres", "postgres", "postgres", "-c search_path=lyfter_car_rental") #Database created and connection made


app = Flask(__name__)


class Users(MethodView):
    def get(self):
        try:
            filter = request.args.get("filter")
            value = request.args.get("value")
            allowed_filters = ["id", "name", "email", "username", "password", "birthday", "status"]
            if not filter:
                get_query = database.execute_query("""
                SELECT * FROM lyfter_car_rental.users
                ORDER BY id ASC
                """)
                return jsonify({"response":get_query}), 200
            if filter not in allowed_filters:
                return jsonify({"error":"This method only accepts id, name, email, username, password, birthday or status."}), 404
            filter_query = database.execute_query(f"""
            SELECT * FROM lyfter_car_rental.users
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
            INSERT INTO lyfter_car_rental.users(name, email, username, password, birthday)
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
            if filter != "id":
                return jsonify({"error":"The filter only accepts id."}), 404
            if update != "status":
                return jsonify({"error":"You can only update the status of a user."}), 404
            database.execute_query(f"""
            UPDATE lyfter_car_rental.users 
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
                SELECT * FROM lyfter_car_rental.vehicles
                ORDER BY id ASC
                """)
                return jsonify({"response":get_query}), 200
            if filter not in allowed_filters:
                return jsonify({"error":"This method only accepts id, make, model, manufacture_year or status."}), 404
            filter_query = database.execute_query(f"""
            SELECT * FROM lyfter_car_rental.vehicles
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
            INSERT INTO lyfter_car_rental.vehicles(make, model, manufacture_year)
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
            if filter != "id":
                return jsonify({"error":"The filter only accepts id."}), 404
            if update != "status":
                return jsonify({"error":"You can only update the status of a vehicle."}), 404
            database.execute_query(f"""
            UPDATE lyfter_car_rental.vehicles 
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
            allowed_filters = ["user_id", "vehicle_id"]
            if not filter:
                get_query = database.execute_query(f"""
                SELECT * FROM lyfter_car_rental.users_vehicles
                ORDER BY id ASC
                """)
                return jsonify({"response":get_query}), 200
            if filter not in allowed_filters:
                return jsonify({"error":"This method only accepts user_id and vehicle id."}), 404
            filter_query = database.execute_query(f"""
            SELECT * FROM lyfter_car_rental.users_vehicles
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
            SELECT status FROM lyfter_car_rental.vehicles
            WHERE id = %s
            """,(data['vehicle_id']))
            car_status = car_status_query[0][0]
            print(car_status)
            if car_status == 'rented':
                return jsonify({"error":"The vehicle you are trying to rent is already rented by an user."}), 400
            elif car_status == 'not available':
                return jsonify({"error":"The vehicle you are trying to rent is not available."}), 400
            database.execute_query("""
            INSERT INTO lyfter_car_rental.users_vehicles(user_id, vehicle_id)
            VALUES (%s, %s)""",(data['user_id'], data['vehicle_id']))
            database.execute_query(f"""
            UPDATE lyfter_car_rental.vehicles
            SET status = 'rented'
            WHERE id = %s
            """,
            (data['vehicle_id']))
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
            if filter != "id":
                return jsonify({"error":"The filter only accepts id."}), 404
            if update != "status":
                return jsonify({"error":"You can only update the status of a rent."}), 404
            if data['status'] != "completed":
                return jsonify({"error":"The status of a rent can only be changed to completed."}), 404
            query_update_status = f"""
            UPDATE lyfter_car_rental.users_vehicles 
            SET {update} = %s
            WHERE {filter} = %s
            """
            query_rent_completed = f"""
            UPDATE lyfter_car_rental.vehicles
            SET {update} = 'available'
            WHERE {filter} = %s
            """
            query_date_completion = f"""
            UPDATE lyfter_car_rental.users_vehicles
            SET rent_devolution_date = CURRENT_DATE
            WHERE {filter} = %s
            """
            database.execute_query(query_update_status, (data[update], value))
            database.execute_query(query_rent_completed, (value))
            database.execute_query(query_date_completion, (value))
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
    app.run(host="localhost", debug=True)