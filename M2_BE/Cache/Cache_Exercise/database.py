from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SqlAlchemyManager:
    def __init__(self, rdbms, user, password, host, port, db_name):
        DB_URI = f"{rdbms}://{user}:{password}@{host}:{port}/{db_name}"
        self.engine = create_engine(DB_URI, echo=False)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def close_connection(self):
        if self.session:
            self.session.close()
            print("Connection closed")