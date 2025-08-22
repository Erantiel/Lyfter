from flask import Flask, jsonify, request
import validations
import files


app = Flask(__name__)


@app.route("/")
def root():
    return "<h1>To start navigating, add the following after the '/': task/read, task/create, task/update, task/delete.</h1>"

@app.route("/task")
def task():
    return "<h1>To start navigating, add the following after the '/': read, create, update, delete.</h1>"

@app.route("/task/read")
def read_tasks():
    tasks = []
    tasks = files.open_json()
    status_filter = request.args.get("status")
    if tasks == []:
        return jsonify(Error="No tasks has been created yet.")
    elif status_filter:
        filtered_tasks = [
            task for task in tasks if task["status"] == status_filter
            ]
        return {f"Tasks filtered by status '{status_filter}'":filtered_tasks}
    else:
        return tasks

@app.route("/task/create", methods=["POST"])
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
        return tasks
    except ValueError as ex:
        return jsonify(Error=str(ex)), 400

@app.route("/task/update/<task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        tasks = []
        tasks = files.open_json()
        found = True
        data = request.json
        counter = 0
        
        if tasks == []:
            return jsonify(Error="No tasks has been created yet.")
        for value in tasks:
            if task_id in value["id"]:
                found = True
                validations.validate_keys(data)
                validations.validate_id(data["id"], tasks)
                validations.validate_title(data)
                validations.validate_description(data)
                validations.validate_status(data)
                tasks[counter] = data
                files.create_json(tasks)
            elif found == False:
                return jsonify(Error="The id does not exists")
            else:
                found = False
                counter += 1
                pass
            
        return tasks
    except ValueError as ex:
        return jsonify(Error=str(ex)), 400


@app.route("/task/delete/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        tasks = []
        tasks = files.open_json()
        found = True
        data = request.json
        counter = 0
        
        if tasks == []:
            return jsonify(Error="No tasks has been created yet.")
        for value in tasks:
            if task_id in value["id"]:
                found = True
                del tasks[counter]
                files.create_json(tasks)
            elif found == False:
                return jsonify(Error="The id does not exists")
            else:
                found = False
                counter += 1
                pass
            
        return tasks
    except ValueError as ex:
        return jsonify(Error=str(ex)), 400


if __name__ == "__main__":
    app.run(host="localhost", debug=True)