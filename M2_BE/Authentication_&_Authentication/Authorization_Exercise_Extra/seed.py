from repositories.role import Role as RoleModel
from repositories.user import User as UserModel


def seed_database(session):

    admin = RoleModel.get_role(session, "Admin")
    customer = RoleModel.get_role(session, "Customer")
    user = UserModel.get_user(session, "Marcelo", "123")

    if admin is None:
        admin = RoleModel.insert_role(session, "Admin")
    if customer is None:
        customer = RoleModel.insert_role(session, "Customer")
    if user is None:
        UserModel.insert_user(
            session,
            "Marcelo",
            "123",
            admin.id
        )
    
    print("Seed created.")