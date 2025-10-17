from flask import Flask, jsonify, request
from flask.views import MethodView
import files


app = Flask(__name__)

class Authetication(MethodView):
    def post(self):
        pass


class Users(MethodView):
    def get(self):
        users = []
        users = files.open_json("users.json")

        return jsonify({"response":users}), 200


    def post(self):
        try:
            users = []
            users = files.open_json("users.json")
            data = request.json

            users.append(data)

            files.create_json(users, "users.json")

            return jsonify({"response":users}), 201
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def put(self, user_id):
        try:
            users = []
            users = files.open_json("users.json")
            data = request.json
            counter = 0

            if users == []:
                return jsonify({"error":"No users have been created yet."}), 400
            for value in users:
                if user_id == value["id"]:
                    if not "id" in data:
                        data["id"] = user_id
                        users[counter] = data
                        files.create_json(users, "users.json")
                        return users, 200
                    else:
                        return jsonify({"error":"Do not include the id in the body when updating a user."}), 400
                elif counter+1 == len(users):
                    return jsonify({"error":"The id does not exist."}), 404
                else:
                    counter += 1
                    pass
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400

    def delete(self, user_id):
        try:
            users = []
            users = files.open_json("users.json")
            counter = 0
            
            if users == []:
                return jsonify({"error":"No users have been created yet."}), 400
            for value in users:
                if user_id == value["id"]:
                    del users[counter]
                    files.create_json(users, "users.json")
                    return "", 204
                elif counter+1 == len(users):
                    return jsonify({"error":"The id does not exist."}), 404
                else:
                    counter += 1
                    pass
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400



users_view = Users.as_view("users_api")
auth_view = Authetication.as_view("auth_api")

app.add_url_rule("/user", methods=["GET", "POST"], view_func=users_view)
app.add_url_rule("/user/<user_id>", methods=["PUT", "DELETE"], view_func=users_view)
app.add_url_rule("/login", methods=["POST"], view_func=auth_view)
app.add_url_rule("/register", methods=["POST"], view_func=auth_view)

app.run(host="localhost", debug=True)