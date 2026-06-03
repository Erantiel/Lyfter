from flask import jsonify, request
from flask.views import MethodView
import files
from database import PgManager


database = PgManager("localhost", 5432, "postgres", "postgres", "postgres", "-c search_path=e_commerce")


class Products(MethodView):
    def get(self):
        try:
            get_query = database.execute_query("""
            SELECT * FROM products
            ORDER BY id ASC
            """)
            database.close_connection()
            return jsonify({"response":get_query}), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def post(self):
        try:
            products = []
            products = files.open_json("products.json")
            data = request.json

            products.append(data)

            files.create_json(products, "products.json")

            return jsonify({"response":products}), 201
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def put(self, product_id):
        try:
            products = []
            products = files.open_json("products.json")
            data = request.json
            counter = 0

            if products == []:
                return jsonify({"error":"No products have been created yet."}), 400
            for value in products:
                if product_id == value["id"]:
                    if not "id" in data:
                        data["id"] = product_id
                        products[counter] = data
                        files.create_json(products, "products.json")
                        return products, 200
                    else:
                        return jsonify({"error":"Do not include the id in the body when updating a product."}), 400
                elif counter+1 == len(products):
                    return jsonify({"error":"The id does not exist."}), 404
                else:
                    counter += 1
                    pass
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


    def delete(self, product_id):
        try:
            products = []
            products = files.open_json("products.json")
            counter = 0
            
            if products == []:
                return jsonify({"error":"No products have been created yet."}), 400
            for value in products:
                if product_id == value["id"]:
                    del products[counter]
                    files.create_json(products, "products.json")
                    return "", 204
                elif counter+1 == len(products):
                    return jsonify({"error":"The id does not exist."}), 404
                else:
                    counter += 1
                    pass
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400


products_view = Products.as_view("products_api")