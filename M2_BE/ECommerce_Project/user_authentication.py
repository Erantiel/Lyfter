from flask import Flask, jsonify, request
from flask.views import MethodView


app = Flask(__name__)

class Authetication(MethodView):
    def post(self):
        pass


class User(MethodView):
    def get(self):
        pass


    def post(self):
        pass


    def put(self):
        pass

    def delete(self):
        pass



user_view = User.as_view("user_api")
auth_view = Authetication.as_view("auth_api")

app.add_url_rule("/user", methods=["GET", "POST", "PUT", "DELETE"], view_func=user_view)
app.add_url_rule("/login", methods=["POST"], view_func=auth_view)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)