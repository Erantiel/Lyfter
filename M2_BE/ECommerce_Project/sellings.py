from flask import Flask, jsonify, request
from flask.views import MethodView


app = Flask(__name__)

class Sellings(MethodView):
    def get(self):
        pass


    def post(self):
        pass


    def put(self):
        pass

    def delete(self):
        pass



sellings_view = Sellings.as_view("sellings_api")

app.add_url_rule("/sellings", methods=["GET", "POST", "PUT", "DELETE"], view_func=sellings_view)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)