from functools import wraps
from flask import request, jsonify

def login_required(jwt_manager):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            token = request.headers.get("Authorization")

            if not token:
                return jsonify({"error": "Token missing"}), 401

            try:
                token = token.replace("Bearer ", "")

                decoded = jwt_manager.decode(token)

                if decoded is None:
                    return jsonify({"error": "Invalid token"}), 401
                
                request.user = decoded

            except Exception as ex:
                return jsonify({"error": str(ex)}), 401

            return func(*args, **kwargs)

        return wrapper
    return decorator


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        user = getattr(request, "user", None)

        if not user:
            return jsonify({"error": "Unauthorized."}), 401

        if user.get("role_id") != 1:
            return jsonify({"error": "Admin access required."}), 403

        return func(*args, **kwargs)

    return wrapper