from flask import Flask, jsonify, request, Response
from flask.views import MethodView
from database import SqlAlchemyManager
from jwt_manager import JWT_Manager
from repositories.bill import Bill as BillModel
from repositories.brand import Brand as BrandModel
from repositories.category import Category as CategoryModel
from repositories.product_bill import ProductBill as PBModel
from repositories.product_shopping_cart import ProductShoppingCart as PSCModel
from repositories.product import Product as ProductModel
from repositories.role import Role as RoleModel
from repositories.shopping_cart import ShoppingCart as SPModel
from repositories.storage_status import StorageStatus as SSModel
from repositories.storage import Storage as StorageModel
from repositories.user import User as UserModel
from base import Base
from exceptions import UniqueDataError
from parsing import to_dict
from seed import seed_database
from validation import validate_all_body_data, validate_body_one_field
from werkzeug.exceptions import UnsupportedMediaType
from decorators import login_required, admin_only


app = Flask("user-service")
db_manager = SqlAlchemyManager("postgresql", "postgres", "postgres", "localhost", "5432", "postgres")
private_key = JWT_Manager.import_private_key_file()
public_key = JWT_Manager.import_public_key_file()
jwt_manager = JWT_Manager(private_key, public_key, "RS256")
Base.metadata.create_all(db_manager.engine)
seed_database(db_manager.session)


class RegisterView(MethodView):
    def post(self):
        try:
            data = request.get_json()

            validate_all_body_data(data, "name", "username", "password", "email")

            UserModel.insert_user(db_manager.session, data.get("name"), data.get("username"), data.get("password"), data.get("email"), 2) # Role_id always 2 since this endpoint only registers customers
            db_manager.close_connection()
            return jsonify("User created."), 200
        except UniqueDataError as ex:
            return jsonify({"error":str(ex)}), 409
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except Exception as ex:
            return jsonify({"error":str(ex)}), 500


class LoginView(MethodView):
    def post(self):
        try:
            data = request.get_json()

            if data is None:
                return Response(status=400)
            
            validate_all_body_data(data, "username", "password")
            
            user = UserModel.login_user(db_manager.session, data.get("username"), data.get("password"))
            user_id = user.id
            role_id = user.role_id
            token = jwt_manager.encode({'id':user_id, "role_id":role_id})
            refresh_token = jwt_manager.encode_refresh_token({'id':user_id, "role_id":role_id})
            UserModel.update_user(db_manager.session, "id", user_id, "refresh_token", refresh_token)
            db_manager.close_connection()
            return jsonify(token=token, refresh_token=refresh_token), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500

class MeView(MethodView):
    @login_required(jwt_manager)
    def get(self):
        try:
            user_id = request.user["id"]
            user = UserModel.get_user_by_id(db_manager.session, user_id)
            db_manager.close_connection()
            return jsonify(id=user_id, name=user.name, username=user.username, email=user.email)
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


class UserView(MethodView):
    @login_required(jwt_manager)
    @admin_only
    def get(self):
        try:
            if request.path.endswith("/all"):
                user = UserModel.get_users(db_manager.session)
                return jsonify([to_dict(user) for user in user])
            
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_body_one_field(data, "id", "name")

            if data.get("id"):
                user = UserModel.get_user_by_id(db_manager.session, data.get("id"))
                db_manager.close_connection()
                return jsonify(to_dict(user)), 200
            elif data.get("name"):
                user = UserModel.get_user_by_name(db_manager.session, data.get("name"))
                db_manager.close_connection()
                return jsonify(to_dict(user)), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500

    @login_required(jwt_manager)
    @admin_only
    def post(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "name", "username", "password", "email", "role_id")

            UserModel.insert_user(db_manager.session, data.get("name"), data.get("username"), data.get("password"), data.get("email"), data.get("role_id")) #Admin can decide the role
            db_manager.close_connection()
            return jsonify("User created."), 200
        except UniqueDataError as ex:
            return jsonify({"error":str(ex)}), 409
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def put(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "filter_column", "filter_value", "update_column", "new_value")
            
            UserModel.update_user(db_manager.session, data.get("filter_column"), data.get("filter_value"), data.get("update_column"), data.get("new_value"))
            db_manager.close_connection()
            return jsonify("User updated."), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def delete(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "filter_column", "filter_value")
            
            UserModel.delete_user(db_manager.session, data.get("filter_column"), data.get("filter_value"))
            db_manager.close_connection()
            return Response(status=204)
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


class ProductView(MethodView):
    @login_required(jwt_manager)
    @admin_only
    def get(self):
        try:
            if request.path.endswith("/all"):
                product = ProductModel.get_products(db_manager.session)
                return jsonify([to_dict(product) for product in product])
            
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_body_one_field(data, "id", "name", "sku")
            
            if data.get("id"):
                product = ProductModel.get_product_by_id(db_manager.session, data.get("id"))
                db_manager.close_connection()
                return jsonify(to_dict(product)), 200
            elif data.get("name"):
                product = ProductModel.get_product_by_name(db_manager.session, data.get("name"))
                db_manager.close_connection()
                return jsonify(to_dict(product)), 200
            elif data.get("sku"):
                product = ProductModel.get_product_by_sku(db_manager.session, data.get("sku"))
                db_manager.close_connection()
                return jsonify(to_dict(product)), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UniqueDataError as ex:
            return jsonify({"error":str(ex)}), 409
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def post(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "sku", "name", "price", "description", "category_id", "brand_id")
            
            ProductModel.insert_product(db_manager.session, data.get("sku"), data.get("name"), data.get("price"), data.get("description"), data.get("category_id"), data.get("brand_id"))
            db_manager.close_connection()
            return jsonify("Product created."), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def put(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "filter_column", "filter_value", "update_column", "new_value")
            
            ProductModel.update_product(db_manager.session, data.get("filter_column"), data.get("filter_value"), data.get("update_column"), data.get("new_value"))
            db_manager.close_connection()
            return jsonify("Product updated."), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def delete(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "filter_column", "filter_value")
            
            ProductModel.delete_product(db_manager.session, data.get("filter_column"), data.get("filter_value"))
            db_manager.close_connection()
            return Response(status=204)
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


class StorageView(MethodView):
    @login_required(jwt_manager)
    @admin_only
    def get(self):
        try:
            if request.path.endswith("/all"):
                storage = StorageModel.get_storage(db_manager.session)
                return jsonify([to_dict(storage) for storage in storage])
            
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_body_one_field(data, "product_id", "id")

            if data.get("id"):
                storage = StorageModel.get_storage_by_id(db_manager.session, data.get("id"))
                db_manager.close_connection()
                return jsonify(to_dict(storage)), 200
            elif data.get("product_id"):
                storage = StorageModel.get_storage_by_product_id(db_manager.session, data.get("product_id"))
                db_manager.close_connection()
                return jsonify(to_dict(storage)), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def post(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "product_id", "amount", "storage_status_id")
            
            StorageModel.insert_storage(db_manager.session, data.get("product_id"), data.get("amount"), data.get("storage_status_id"))
            return jsonify("Item added to the storage."), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def put(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "filter_column", "filter_value", "update_column", "new_value")
            
            StorageModel.update_storage(db_manager.session, data.get("filter_column"), data.get("filter_value"), data.get("update_column"), data.get("new_value"))
            db_manager.close_connection()
            return jsonify("Storage updated."), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def delete(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "filter_column", "filter_value")
            
            StorageModel.delete_storage(db_manager.session, data.get("filter_column"), data.get("filter_value"))
            db_manager.close_connection()
            return Response(status=204)
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


class BillView(MethodView):
    @login_required(jwt_manager)
    def get(self):
        try:
            user_id = request.user["id"]
            role_id = request.user["role_id"]

            if role_id == 1:
                if request.path.endswith("/all"):
                    bills = BillModel.get_bills(db_manager.session)
                    return jsonify([to_dict(bills) for bills in bills])
            
                data = request.get_json()

                if not data:
                    return Response(status=400)
                
                validate_body_one_field(data, "id", "user_id")
                
                if data.get("id"):
                    bill = BillModel.get_bill_by_id(db_manager.session, data.get("id"))
                    db_manager.close_connection()
                    return jsonify(to_dict(bill)), 200
                if data.get("user_id"):
                    bill = BillModel.get_bill_by_id(db_manager.session, data.get("user_id"))
                    db_manager.close_connection()
                    return jsonify(to_dict(bill)), 200
            elif role_id == 2:
                bill = BillModel.get_bills_by_user_id(db_manager.session, user_id)
                db_manager.close_connection()
                return jsonify([to_dict(bills) for bills in bills]), 200
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


    @login_required(jwt_manager)
    @admin_only
    def delete(self):
        try:
            data = request.get_json()

            if not data:
                return Response(status=400)
            
            validate_all_body_data(data, "filter_column", "filter_value")
            
            BillModel.delete_bill(db_manager.session, data.get("filter_column"), data.get("filter_value"))
            db_manager.close_connection()
            return Response(status=204)
        except ValueError as ex:
            return jsonify({"error":str(ex)}), 400
        except UnsupportedMediaType as ex:
            return jsonify({"error":str(ex)}), 415
        except Exception as ex:
            db_manager.session.rollback()
            return jsonify({"error":str(ex)}), 500


class RefreshTokenView(MethodView):
    def post(self):
        try:
            data = request.get_json()
            refresh_token = data.get("refresh_token")

            if not refresh_token:
                return jsonify({
                    "error": "Refresh token required."
                }), 400

            decoded = jwt_manager.decode(refresh_token)

            if decoded is None:
                return jsonify({
                    "error": "Invalid or expired refresh token."
                }), 401

            if decoded.get("type") != "refresh":
                return jsonify({
                    "error": "Invalid token type."
                }), 401

            new_access_token = jwt_manager.encode({
                "id": decoded.get("id"),
                "role_id": decoded.get("role_id")
            })

            return jsonify({"New token": new_access_token}), 200

        except Exception as e:
            print("REFRESH ERROR:", e)
            return jsonify({
                "error": "Server error"
            }), 500


register_view = RegisterView.as_view("register_view_api")
login_view = LoginView.as_view("login_view_api")
me_view = MeView.as_view("me_view_api")
user_view = UserView.as_view("user_view_api")
product_view = ProductView.as_view("product_view_api")
storage_view = StorageView.as_view("storage_view_api")
bill_view = BillView.as_view("bill_view.api")
refresh_token_view = RefreshTokenView.as_view("refresh_token_view.api")

app.add_url_rule("/register", methods=["POST"], view_func=register_view)
app.add_url_rule("/login", methods=["POST"], view_func=login_view)
app.add_url_rule("/me", methods=["GET"], view_func=me_view)
app.add_url_rule("/user", methods=["GET", "POST", "PUT", "DELETE"], view_func=user_view)
app.add_url_rule("/user/all", methods=["GET"], view_func=user_view)
app.add_url_rule("/product", methods=["GET", "POST", "PUT", "DELETE"], view_func=product_view)
app.add_url_rule("/product/all", methods=["GET"], view_func=product_view)
app.add_url_rule("/storage", methods=["GET", "POST", "PUT", "DELETE"], view_func=storage_view)
app.add_url_rule("/storage/all", methods=["GET"], view_func=storage_view)
app.add_url_rule("/bill", methods=["GET", "DELETE"], view_func=bill_view)
app.add_url_rule("/bil/all", methods=["GET"], view_func=bill_view)
app.add_url_rule("/refresh-token", methods=["POST"], view_func=refresh_token_view)

if __name__ == "__main__":
    app.run(host="localhost", debug=True, use_reloader=False, port=5000)