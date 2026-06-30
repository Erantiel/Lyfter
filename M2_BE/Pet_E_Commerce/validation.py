def validate_all_body_data(data, *args):
    if not all(key in data for key in args):
        raise ValueError("Body data incorrect.")
    else:
        return True


def validate_body_one_field(data, *args):

    if not any(key in data for key in args): 
        raise ValueError("Body data incorrect.")
    if len(data) != 1:
        raise ValueError("The body accepts only one data at a time.")
    else:
        return True