from database import SqlAlchemyManager

database = SqlAlchemyManager("postgresql", "postgres", "postgres", "localhost", "5432", "postgres")
database.create_all_tables()
database.close_connection()