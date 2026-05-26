from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert, update, delete, select

class SqlAlchemyManager:
    def __init__(self, rdbms, user, password, host, port, db_name):
        self.rdbms=rdbms
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db_name=db_name

        self.session=None
        self.engine=None
        self.metadata_obj=MetaData(schema="orm")

        self.connection = self.create_connection(rdbms, user, password, host, port, db_name)

    def create_connection(self, rdbms, user, password, host, port, db_name):
        try:
            DB_URI = f"{rdbms}://{user}:{password}@{host}:{port}/{db_name}"
            self.engine = create_engine(DB_URI, echo=True)
            self.session = self.engine.connect()
            print("Connection successful!")
            return DB_URI
        except Exception as error:
            print("Error connecting to the database:", error)
            return None


    def close_connection(self):
        if self.session:
            self.session.close()
            print("Connection closed")


# Create Tables ---------------------------------------
    def create_user_table(self):
        self.user_table = Table(
            "user",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("name", String(30), nullable=False),
            autoload_with=self.engine
        )


    def create_address_table(self):
        self.address_table = Table(
            "address",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("address", String(100), nullable=False),
            Column("user_id", ForeignKey("orm.user.id"), nullable=False)
        )


    def create_vehicle_table(self):
        self.vehicle_table = Table(
            "vehicle",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("make", String(100), nullable=False),
            Column("user_id", ForeignKey("orm.user.id"), nullable=True)
        )


    def create_all_tables(self):
        self.create_user_table()
        self.create_address_table()
        self.create_vehicle_table()
        self.metadata_obj.create_all(self.engine)


# User ---------------------------------------
    def insert_user(self, name):
        query = insert(self.user_table).values(name=name)       
        self.session.execute(query)
        self.session.commit()


    def update_user(self, where_column, old_value, update_column, new_value):
        query = (update(self.user_table)
        .where(getattr(self.user_table.c, where_column) == old_value)
        .values({update_column:new_value}))      
        self.session.execute(query)
        self.session.commit()


    def delete_user(self, where_column, value):
        query = (delete(self.user_table)
        .where(getattr(self.user_table.c, where_column) == value))
        self.session.execute(query)
        self.session.commit()


    def select_user(self):
            query = select(self.user_table)
            result = self.session.execute(query)
            self.session.commit()
            for row in result:
                print(row)


# Address ---------------------------------------
    def insert_address(self, address, user_id):
        query = insert(self.address_table).values(address=address, user_id=user_id)       
        self.session.execute(query)
        self.session.commit()


    def update_address(self, where_column, old_value, update_column, new_value):
        query = (update(self.address_table)
        .where(getattr(self.address_table.c, where_column) == old_value)
        .values({update_column:new_value}))      
        self.session.execute(query)
        self.session.commit()


    def delete_address(self, where_column, value):
        query = (delete(self.address_table)
        .where(getattr(self.address_table.c, where_column) == value))
        self.session.execute(query)
        self.session.commit()


    def select_address(self):
            query = select(self.address_table)
            result = self.session.execute(query)
            self.session.commit()
            for row in result:
                print(row)


# Vehicle ---------------------------------------
    def insert_vehicle(self, make, user_id=None):
        query = insert(self.vehicle_table).values(make=make, user_id=user_id)       
        self.session.execute(query)
        self.session.commit()


    def update_vehicle(self, where_column, old_value, update_column, new_value):
        query = (update(self.vehicle_table)
        .where(getattr(self.vehicle_table.c, where_column) == old_value)
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
        for row in result:
            print(row)
