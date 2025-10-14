from flask import Flask, jsonify, request
from flask.views import MethodView


app = Flask(__name__)

class Products(MethodView):
    def get(self):
        pass


    def post(self):
        pass


    def put(self):
        pass

    def delete(self):
        pass



products_view = Products.as_view("products_api")

app.add_url_rule("/products", methods=["GET", "POST", "PUT", "DELETE"], view_func=products_view)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)