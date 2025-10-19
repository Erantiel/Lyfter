from flask import Flask
from users import users_view, auth_view
from sellings import sellings_view
from products import products_view


app = Flask(__name__)


# Products URLs
app.add_url_rule("/products", methods=["GET", "POST"], view_func=products_view)
app.add_url_rule("/products/<product_id>", methods=["PUT", "DELETE"], view_func=products_view)


# Sellings URLs
app.add_url_rule("/sellings", methods=["GET", "POST"], view_func=sellings_view)
app.add_url_rule("/sellings/<selling_id>", methods=["PUT", "DELETE"], view_func=sellings_view)


# Users URLs
app.add_url_rule("/users", methods=["GET", "POST"], view_func=users_view)
app.add_url_rule("/users/<user_id>", methods=["PUT", "DELETE"], view_func=users_view)
app.add_url_rule("/login", methods=["POST"], view_func=auth_view)
app.add_url_rule("/register", methods=["POST"], view_func=auth_view)


if __name__ == "__main__":
    app.run(debug=True)