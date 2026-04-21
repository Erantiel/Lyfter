import psycopg2

class PgManager:
    def __init__(self, host, port, user, password, db_name, options):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db_name=db_name
        self.options=options

        self.connection = self.create_connection(host, port, user, password, db_name, options)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")


    def create_connection(self, host, port, user, password, db_name, options):
        try:
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.db_name,
                options=self.options,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None


    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")


    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()

            if self.cursor.description:
                return self.cursor.fetchall()
            
        except psycopg2.errors.DuplicateTable as error:
            pass
        except Exception as error:
            self.connection.rollback()   # important
            print(error)