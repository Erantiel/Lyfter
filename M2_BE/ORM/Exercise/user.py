from sqlalchemy import Table, Column, Integer, String, insert, update, delete, select, func

class User:
    def __init__(self, session, metadata_obj, engine):
        self.session=session
        self.metadata_obj=metadata_obj
        self.engine=engine
        self.create_user_table()

    def create_user_table(self):
        self.user_table = Table(
            "user",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("name", String(30), nullable=False),
        )
        self.metadata_obj.create_all(self.engine)


    def insert_user(self, name):
        query = insert(self.user_table).values(name=name)       
        self.session.execute(query)
        self.session.commit()


    def update_user(self, where_column, where_value, update_column, new_value):
        query = (update(self.user_table)
        .where(getattr(self.user_table.c, where_column) == where_value)
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
        return result.fetchall()