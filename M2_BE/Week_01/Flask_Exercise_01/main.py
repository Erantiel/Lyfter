from flask import Flask, jsonify, request
import validations
import files


app = Flask(__name__)


@app.route("/")
def root():
    return "<h1>To start navigating, add the following after the '/': GET/tasks, POST/tasks, PUT/tasks/<task_id>, DELETE/tasks/task_id.</h1>"

@app.route("/GET/tasks")
def read_tasks():
    tasks = []
    tasks = files.open_json()
    status_filter = request.args.get("status")
    if tasks == []:
        return jsonify(Error="No tasks has been created yet."), 404
    elif not status_filter:
        return tasks, 200
    elif status_filter == "Completed" or status_filter == "Pending" or status_filter == "Ongoing":
        filtered_tasks = [
            task for task in tasks if task["status"] == status_filter
            ]
        if filtered_tasks == []:
            return jsonify(Error="No tasks with the current status exists."), 404
        else:
            return {f"Tasks filtered by status '{status_filter}'":filtered_tasks}, 200
    else:
        return jsonify(Error="This method only accepts Completed, Pending or Ongoing as status"), 400

@app.route("/POST/tasks", methods=["POST"])
def create_task():
    try:
        tasks = []
        tasks = files.open_json()
        data = request.json

        validations.validate_keys(data)
        validations.validate_id(data["id"], tasks)
        validations.validate_title(data)
        validations.validate_description(data)
        validations.validate_status(data)
        
        tasks.append({
            "id":data["id"],
            "title":data["title"],
            "description":data["description"],
            "status":data["status"]
        })
        files.create_json(tasks)
        return tasks, 201
    except ValueError as ex:
        return jsonify(Error=str(ex)), 400

@app.route("/PUT/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        tasks = []
        tasks = files.open_json()
        data = request.json
        counter = 0
        
        if tasks == []:
            return jsonify(Error="No tasks has been created yet.")
        for value in tasks:
            if task_id == value["id"]:
                if not "id" in data:
                    validations.validate_title(data)
                    validations.validate_description(data)
                    validations.validate_status(data)
                    tasks[counter]["id"] = task_id
                    tasks[counter]["title"] = data["title"]
                    tasks[counter]["description"] = data["description"]
                    tasks[counter]["status"] = data["status"]
                    files.create_json(tasks)
                    return tasks, 200
                else:
                    return jsonify(Error="Do not include the id in the body when updating the task."), 400
            elif counter+1 == len(tasks):
                return jsonify(Error="The id does not exist."), 404
            else:
                counter += 1
                pass
    except ValueError as ex:
        return jsonify(Error=str(ex)), 400


@app.route("/DELETE/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        tasks = []
        tasks = files.open_json()
        counter = 0
        
        if tasks == []:
            return jsonify(Error="No tasks has been created yet."), 400
        for value in tasks:
            if task_id == value["id"]:
                del tasks[counter]
                files.create_json(tasks)
                return jsonify(msg="Sucesfull deletion."), 204
            elif counter+1 == len(tasks):
                return jsonify(Error="The id does not exist."), 404
            else:
                counter += 1
                pass
    except ValueError as ex:
        return jsonify(Error=str(ex)), 400


if __name__ == "__main__":
    app.run(host="localhost", debug=True)