from flask import Flask, jsonify, request
from flask.views import MethodView
import validations
import files
import secrets


app = Flask(__name__)

user = {"username":"admin","password":"1234"}
token = {}

def check_token(func):
    def wrapper(*args,**kwargs):
        header_token = request.headers.get("Authorization", "")
        if not header_token.startswith("Bearer "):
            return jsonify({"error":"Incorrect header format. Try: Authorization: Bearer <token>"}), 401
        
        received_token = header_token.split(" ")[1]

        if token["value"] != received_token:
            return jsonify({"error":"Invalid token"}), 401
        return func(*args,**kwargs)
    


class Authetication(MethodView):
    def post(self):
        global token
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if user["username"] != username or user["password"] != password:
            return jsonify({"error":"Invalid credentials"}), 401
        
        generated_token = secrets.token_hex(16)
        token["value"] = generated_token
        return jsonify({"token":generated_token}), 200


class Tasks(MethodView):
    @check_token
    def get(self):
        tasks = []
        tasks = files.open_json()
        status_filter = request.args.get("status")
        if tasks == []:
            return jsonify([]), 200
        elif not status_filter:
            return tasks, 200
        elif status_filter == "Completed" or status_filter == "Pending" or status_filter == "Ongoing":
            filtered_tasks = [
                task for task in tasks if task["status"] == status_filter
                ]
            if filtered_tasks == []:
                return jsonify({"error":"No tasks with the current status exists."}), 200
            else:
                return jsonify({"response":f"Tasks filtered by status '{status_filter}':{filtered_tasks}"}), 200
        else:
            return jsonify({"error":"This method only accepts Completed, Pending or Ongoing as status"}), 404


    @check_token
    def post(self):
        try:
            tasks = []
            tasks = files.open_json()
            data = request.json

            validations.validate_data(data["id"], tasks, data)
            
            tasks.append(validations.data_structure(data))
            files.create_json(tasks)
            return jsonify({"response":tasks}), 201
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    @check_token
    def put(self, task_id):
        try:
            tasks = []
            tasks = files.open_json()
            data = request.json
            counter = 0
            
            if tasks == []:
                return jsonify({"error":"No tasks has been created yet."}), 400
            for value in tasks:
                if task_id == value["id"]:
                    if not "id" in data:
                        validations.validate_data("", tasks, data)
                        data["id"] = task_id
                        tasks[counter] = validations.data_structure(data)
                        files.create_json(tasks)
                        return tasks, 200
                    else:
                        return jsonify({"error":"Do not include the id in the body when updating the task."}), 400
                elif counter+1 == len(tasks):
                    return jsonify({"error":"The id does not exist."}), 404
                else:
                    counter += 1
                    pass
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    @check_token
    def delete(self, task_id):
        try:
            tasks = []
            tasks = files.open_json()
            counter = 0
            
            if tasks == []:
                return jsonify({"error":"No tasks has been created yet."}), 400
            for value in tasks:
                if task_id == value["id"]:
                    del tasks[counter]
                    files.create_json(tasks)
                    return "", 204
                elif counter+1 == len(tasks):
                    return jsonify({"error":"The id does not exist."}), 404
                else:
                    counter += 1
                    pass
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400



task_view = Tasks.as_view("tasks_api")
auth_view = Authetication.as_view("auth_api")

app.add_url_rule("/task", methods=["GET", "POST"], view_func=task_view)
app.add_url_rule("/task/<task_id>", methods=["PUT", "DELETE"], view_func=task_view)
app.add_url_rule("/login", methods=["POST"], view_func=auth_view)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)