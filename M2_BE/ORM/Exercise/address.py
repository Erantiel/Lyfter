from sqlalchemy import Table, Column, Integer, String, ForeignKey, insert, update, delete, select

class Address:
    def __init__(self, session, metadata_obj, engine):
        self.session=session
        self.metadata_obj=metadata_obj
        self.engine=engine
        self.create_address_table()

    def create_address_table(self):
        self.address_table = Table(
            "address",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("address", String(100), nullable=False),
            Column("user_id", ForeignKey("orm.user.id"), nullable=False)
        )
        self.metadata_obj.create_all(self.engine)


    def insert_address(self, address, user_id):
        query = insert(self.address_table).values(address=address, user_id=user_id)       
        self.session.execute(query)
        self.session.commit()


    def update_address(self, where_column, where_value, update_column, new_value):
        query = (update(self.address_table)
        .where(getattr(self.address_table.c, where_column) == where_value)
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
        return result.fetchall()