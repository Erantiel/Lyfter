def validate_keys_users(data):
    if "name" not in data:
        raise ValueError("Key 'name' is missing from the dictionary.")
    if "email" not in data:
        raise ValueError("Key 'email' is missing from the dictionary.")
    if "username" not in data:
        raise ValueError("Key 'username' is missing from the dictionary.")
    if "password" not in data:
        raise ValueError("Key 'password' is missing from the dictionary.")
    if "birthday" not in data:
        raise ValueError("Key 'birthday' is missing from the dictionary.")
    for key in data:
        if key == "name" or key == "email" or key == "username" or key == "password" or key == "birthday":
            pass
        else:
            raise ValueError("The body can only contain the following keys: name, email, username, password and birthday.")
    return data


def validate_data_users(data):
    if data["name"] == "":
        raise ValueError("The name cannot be empty.")
    if data["email"] == "":
        raise ValueError("The email cannot be empty.")
    if data["username"] == "":
        raise ValueError("The username cannot be empty.")
    if data["password"] == "":
        raise ValueError("The password cannot be empty.")
    if data["birthday"] == "":
        raise ValueError("The birthday cannot be empty.")


def validate_keys_vehicles(data):
    if "make" not in data:
        raise ValueError("Key 'make' is missing from the dictionary.")
    if "model" not in data:
        raise ValueError("Key 'model' is missing from the dictionary.")
    if "manufacture_year" not in data:
        raise ValueError("Key 'manufacture_year' is missing from the dictionary.")
    for key in data:
        if key == "make" or key == "model" or key == "manufacture_year":
            pass
        else:
            raise ValueError("The body can only contain the following keys: make, model and manufacture_year.")
    return data


def validate_data_vehicles(data):
    if data["make"] == "":
        raise ValueError("The make cannot be empty.")
    if data["model"] == "":
        raise ValueError("The model cannot be empty.")
    if data["manufacture_year"] == "":
        raise ValueError("The manufacture_year cannot be empty.")


def validate_keys_users_vehicles(data):
    if "user_id" not in data:
        raise ValueError("Key 'user_id' is missing from the dictionary.")
    if "vehicle_id" not in data:
        raise ValueError("Key 'vehicle_id' is missing from the dictionary.")
    for key in data:
        if key == "user_id" or key == "vehicle_id":
            pass
        else:
            raise ValueError("The body can only contain the following keys: user_id and vehicle_id.")
    return data


def validate_data_users_vehicles(data):
    if data["user_id"] == "":
        raise ValueError("The user_id cannot be empty.")
    if data["vehicle_id"] == "":
        raise ValueError("The vehicle_id cannot be empty.")