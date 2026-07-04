from repositories.role import Role as RoleModel
from repositories.user import User as UserModel


def seed_database(session):

    admin = RoleModel.get_role_by_name(session, "Admin")
    customer = RoleModel.get_role_by_name(session, "Customer")
    user = UserModel.get_user_by_name(session, "Marcelo")

    if admin is None:
        admin = RoleModel.insert_role(session, "Admin")
    if customer is None:
        customer = RoleModel.insert_role(session, "Customer")
    if user is None:
        UserModel.insert_user(
            session,
            "Marcelo",
            "marc962",
            "123",
            "alfaom@gmail.com",
            admin.id
        )
        print("Seed created.")