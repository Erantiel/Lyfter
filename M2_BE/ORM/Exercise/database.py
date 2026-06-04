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
