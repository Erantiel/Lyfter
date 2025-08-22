def validate_keys(data):
    if "id" not in data:
        raise ValueError("id key is missing from the dictionary.")
    if "title" not in data:
        raise ValueError("title key is missing from the dictionary.")
    if "description" not in data:
        raise ValueError("description key is missing from the dictionary.")
    if "status" not in data:
        raise ValueError("status key is missing from the dictionary.")


def validate_id(id_dic, tasks):
    for task in tasks:
        for key,value in task.items():
            if id_dic == value:
                raise ValueError("The id already exists. Type a new one.")
    if id_dic == "":
        raise ValueError("The id cannot be empty")


def validate_title(data):
    if data["title"] == "":
        raise ValueError("The title cannot be empty")


def validate_description(data):
    if data["description"] == "":
        raise ValueError("The description cannot be empty")    


def validate_status(data):
    if data["status"] == "":
        raise ValueError("The status cannot be empty")
    elif data["status"] == "Pending" or data["status"] == "Ongoing" or data["status"] == "Completed":
        pass
    else:
        raise ValueError("The status can only be: 'Pending', 'Ongoing' or 'Completed'")