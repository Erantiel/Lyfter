from sqlalchemy import Table, Column, Integer, String, ForeignKey, insert, update, delete, select

class Vehicle:
    def __init__(self, session, metadata_obj, engine):
        self.session=session
        self.metadata_obj=metadata_obj
        self.engine=engine
        self.create_vehicle_table()

    def create_vehicle_table(self):
        self.vehicle_table = Table(
            "vehicle",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("make", String(100), nullable=False),
            Column("user_id", ForeignKey("orm.user.id"), nullable=True)
        )
        self.metadata_obj.create_all(self.engine)

    def insert_vehicle(self, make, user_id=None):
        query = insert(self.vehicle_table).values(make=make, user_id=user_id)       
        self.session.execute(query)
        self.session.commit()


    def update_vehicle(self, where_column, where_value, update_column, new_value):
        query = (update(self.vehicle_table)
        .where(getattr(self.vehicle_table.c, where_column) == where_value)
        .values({update_column:new_value}))      
        self.session.execute(query)
        self.session.commit()


    def delete_vehicle(self, where_column, value):
        query = (delete(self.vehicle_table)
        .where(getattr(self.vehicle_table.c, where_column) == value))
        self.session.execute(query)
        self.session.commit()


    def select_vehicle(self):
        query = select(self.vehicle_table)
        result = self.session.execute(query)
        self.session.commit()
        return result.fetchall()


    def associate_vehicle_user(self, where_column, where_value, new_value):
        query = (update(self.vehicle_table)
        .where(getattr(self.vehicle_table.c, where_column) == where_value)
        .values({"user_id":new_value}))
        self.session.execute(query)
        self.session.commit()