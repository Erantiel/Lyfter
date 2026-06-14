from flask import Flask, jsonify, request, Response
from flask.views import MethodView
from database import SqlAlchemyManager
from jwt_manager import JWT_Manager
from repositories.bill import Bill as BillModel
from repositories.product import Product as ProductModel
from repositories.role import Role as RoleModel
from repositories.storage import Storage as StorageModel
from repositories.user import User as UserModel
from base import Base
from exceptions import DuplicateUsernameError
from parsing import to_dict
from seed import seed_database


app = Flask("user-service")
db_manager = SqlAlchemyManager("postgresql", "postgres", "postgres", "localhost", "5432", "postgres")
private_key = JWT_Manager.import_private_key_file()
public_key = JWT_Manager.import_public_key_file()
jwt_manager = JWT_Manager(private_key, public_key, "RS256")
Base.metadata.create_all(db_manager.engine)
seed_database(db_manager.session)

class Register(MethodView):
    def post(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]
            data = request.get_json()

            if(data.get('username') == None or data.get('password') == None):
                return Response(status=400)
            if role_id == 1:
                result = UserModel.insert_user(db_manager.session, data.get('username'), data.get('password'), data.get("role_id"))
                user_id = result.id
                role_id = result.role_id
                token = jwt_manager.encode({'id':user_id, "role_id":role_id})
                db_manager.close_connection()
                return jsonify(token=token), 200
            else:
                result = UserModel.insert_user(db_manager.session, data.get('username'), data.get('password'), 2)
                user_id = result.id
                role_id = result.role_id
                token = jwt_manager.encode({'id':user_id, "role_id":role_id})
                db_manager.close_connection()
                return jsonify(token=token), 200

        except DuplicateUsernameError as ex:
            return jsonify({"error":str(ex)}), 409
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as ex:
            return jsonify({"error":str(ex)}), 500


class Login(MethodView):
    def post(self):
        try:
            data = request.get_json()
            if(data.get('username') == None or data.get('password') == None):
                return Response(status=400)
            else:
                result = UserModel.get_user(db_manager.session, data.get('username'), data.get('password'))
                db_manager.close_connection()
                if(result == None):
                    return Response(status=403)
                else:
                    user_id = result.id
                    role_id = result.role_id
                    token = jwt_manager.encode({'id':user_id, "role_id":role_id})
                
                    return jsonify(token=token), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as ex:
            return jsonify({"error":str(ex)}), 500


class Me(MethodView):
    def get(self):
        try:
            token = request.headers.get('Authorization')
            if(token is not None):
                test = token.replace("Bearer ","")
                decoded = jwt_manager.decode(test)
                user_id = decoded['id']
                if decoded is None:
                    return Response(status=401)
                user = UserModel.get_user_by_id(db_manager.session, user_id)
                db_manager.close_connection()
                return jsonify(id=user_id, username=user.username)
            else:
                return Response(status=403)
        except Exception as ex:
            return jsonify({"error":str(ex)}), 500


class UserView(MethodView):
    def put(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]
            data = request.get_json()
            
            if role_id == 1:
                if not data:
                    return Response(status=400)
                UserModel.update_user(db_manager.session, data.get("filter_column"), data.get("filter_value"), data.get("update_column"), data.get("new_value"))
                db_manager.close_connection()
                return jsonify("User updated."), 200
            else:
                return jsonify("You do not have the rights to edit users."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            return Response(status=500)


    def delete(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]
            data = request.get_json()

            if role_id == 1:
                if not data:
                    return Response(status=400)
                UserModel.delete_user(db_manager.session, data.get("filter_column"), data.get("filter_value"))
                db_manager.close_connection()
                return Response(status=204)
            else:
                return jsonify("You do not have the rights to delete users."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            return Response(status=500)


class ProductView(MethodView):
    def get(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]

            if role_id == 1:
                data = request.get_json()
                if not data:
                    return Response(status=400)
                if data.get("id"):
                    product = ProductModel.get_product_by_id(db_manager.session, data.get("id"))
                    db_manager.close_connection()
                    return jsonify(to_dict(product)), 200
                product = ProductModel.get_product(db_manager.session, data.get("name"))
                db_manager.close_connection()
                return jsonify(to_dict(product)), 200
            else:
                return jsonify("You do not have the rights to view products."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            print(e)
            return Response(status=500)


    def post(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]

            data = request.get_json()
            if role_id == 1:
                if not data:
                    return Response(status=400)
                ProductModel.insert_product(db_manager.session, data.get("name"), data.get("price"))
                return jsonify("Product created."), 200
            else:
                return jsonify("You do not have the rights to add products."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            return Response(status=500)


    def put(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]

            data = request.get_json()
            if role_id == 1:
                if not data:
                    return Response(status=400)
                ProductModel.update_product(db_manager.session, data.get("filter_column"), data.get("filter_value"), data.get("update_column"), data.get("new_value"))
                db_manager.close_connection()
                return jsonify("Product updated."), 200
            else:
                return jsonify("You do not have the rights to update products."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            return Response(status=500)


    def delete(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]

            if role_id == 1:
                data = request.get_json()
                if not data:
                    return Response(status=400)
                ProductModel.delete_product(db_manager.session, data.get("filter_column"), data.get("filter_value"))
                db_manager.close_connection()
                return Response(status=204)
            else:
                return jsonify("You do not have the rights to delete products."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception:
            return Response(status=500)


class StorageView(MethodView):
    def get(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]

            if role_id == 1:
                data = request.get_json()
                if not data:
                    return Response(status=400)
                if data.get("id"):
                    storage = StorageModel.get_storage_by_id(db_manager.session, data.get("id"))
                    db_manager.close_connection()
                    return jsonify(to_dict(storage)), 200
                else:
                    storage = StorageModel.get_storage(db_manager.session)
                    db_manager.close_connection()
                    return jsonify([to_dict(storage) for storage in storage]), 200
            else:
                return jsonify("You do not have the rights to add to view the storage."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            return Response(status=500)


    def post(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]
            data = request.get_json()

            if role_id == 1:
                if not data:
                    return Response(status=400)
                StorageModel.insert_storage(db_manager.session, data.get("product_id"), data.get("amount"))
                return jsonify("Item added to the storage."), 200
            else:
                return jsonify("You do not have the rights to add to the storage."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            return Response(status=500)


    def put(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]
            data = request.get_json()

            if role_id == 1:
                if not data:
                    return Response(status=400)
                StorageModel.update_storage(db_manager.session, data.get("filter_column"), data.get("filter_value"), data.get("update_column"), data.get("new_value"))
                db_manager.close_connection()
                return jsonify("Storage updated."), 200
            else:
                return jsonify("You do not have the rights to add update the storage."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            return Response(status=500)


    def delete(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]
            data = request.get_json()

            if role_id == 1:
                if not data:
                    return Response(status=400)
                StorageModel.delete_storage(db_manager.session, data.get("filter_column"), data.get("filter_value"))
                db_manager.close_connection()
                return Response(status=204)
            else:
                return jsonify("You do not have the rights to add delete from the storage."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception:
            return Response(status=500)


class BillView(MethodView):
    def get(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)
            user_id = decoded["id"]
            role_id = decoded["role_id"]

            if decoded is None:
                return Response(status=401)

            data = request.get_json()

            if role_id == 1:
                if data.get("id"):
                    bill = BillModel.get_bill_by_id(db_manager.session, data.get("id"))
                    db_manager.close_connection()
                    return jsonify(to_dict(bill)), 200
                else:
                    bills = BillModel.get_bills(db_manager.session)
                    db_manager.close_connection()
                    return jsonify([to_dict(bills) for bills in bills]), 200
            elif role_id == 2:
                bill = BillModel.get_bills_by_user_id(db_manager.session, user_id)
                db_manager.close_connection()
                return jsonify([to_dict(bills) for bills in bills]), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            return Response(status=500)


    def post(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            user_id = decoded["id"]
            
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            storage = StorageModel.get_storage_by_product_id(db_manager.session, data.get("product_id"))
            storage_availabilty = storage.amount
            new_value = storage_availabilty - data.get("product_amount")
            if data.get("product_amount") <= storage_availabilty:
                BillModel.insert_bill(db_manager.session, user_id, data.get("product_id"), data.get("product_amount"))
                StorageModel.update_storage(db_manager.session, "id", data.get("product_id"), "amount", new_value)
                return jsonify("Bill generated."), 200
            else:
                return jsonify(f"There are not enough reserves to place an order."), 400
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as e:
            print(e)
            return Response(status=500)


    def delete(self):
        try:
            token = request.headers.get("Authorization")
            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)

            if decoded is None:
                return Response(status=401)

            role_id = decoded["role_id"]

            if role_id == 1:
                data = request.get_json()
                if not data:
                    return Response(status=400)
                BillModel.delete_bill(db_manager.session, data.get("filter_column"), data.get("filter_value"))
                db_manager.close_connection()
                return Response(status=204)
            else:
                return jsonify("You do not have the rights to delete a bill."), 403
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception:
            return Response(status=500)



register_view = Register.as_view("register_api")
login_view = Login.as_view("login_api")
me_view = Me.as_view("me_api")
user_view = UserView.as_view("user_view_api")
product_view = ProductView.as_view("product_view_api")
storage_view = StorageView.as_view("storage_view_api")
bill_view = BillView.as_view("bill_view.api")

app.add_url_rule("/register", methods=["POST"], view_func=register_view)
app.add_url_rule("/login", methods=["POST"], view_func=login_view)
app.add_url_rule("/me", methods=["GET"], view_func=me_view)
app.add_url_rule("/user", methods=["PUT", "DELETE"], view_func=user_view)
app.add_url_rule("/product", methods=["GET", "POST", "PUT", "DELETE"], view_func=product_view)
app.add_url_rule("/storage", methods=["GET", "POST", "PUT", "DELETE"], view_func=storage_view)
app.add_url_rule("/bill", methods=["GET", "POST", "PUT", "DELETE"], view_func=bill_view)

if __name__ == "__main__":
    app.run(host="localhost", debug=True, use_reloader=False, port=5000)