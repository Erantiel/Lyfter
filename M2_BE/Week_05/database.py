import psycopg2
from datetime import datetime
import os
from faker import Faker
from faker.providers import DynamicProvider
import random

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
    

    def backup_export_database(self, filename, table_path):
        current_date = datetime.now().strftime("%Y-%m-%d")
        folder_path = f"db_backups/backup_{current_date}"
        os.makedirs(folder_path, exist_ok=True)
        file_path = f"{folder_path}/{filename}"

        with open(file_path, "w", encoding="utf-8") as file:
            self.cursor.copy_expert(
                f'COPY {table_path} TO STDOUT WITH CSV HEADER', file
            )


    def check_table_exists(self, data, table_name):
        self.cursor.execute("""
        SELECT to_regclass(%s)
        """,(table_name,))

        table_exists = self.cursor.fetchone()[0]

        if table_exists:
            self.cursor.execute(f"""
            SELECT COUNT(*) FROM {table_name}
            """)

            data_exists = self.cursor.fetchone()[0]

            if data_exists > 0:
                print(f"--Table {table_name} exists and has {data} in it.--")
            else:
                print(f"--Table {table_name} exists and has no {data} in it.--")
        else:
            print(f"--Table {table_name} does not exists.--")


    def faker_users(self, loop):
        fake = Faker()
        for r in range(loop):
            self.cursor.execute(f"""INSERT INTO lyfter_car_rental.users(name, email, username, password, birthday, overdue)
                                VALUES (%s, %s, %s, %s, %s, %s)
            """,(
            fake.name(),
            fake.email(),
            fake.user_name(),
            fake.password(),
            fake.date_of_birth(),
            fake.boolean()
            ))
        self.connection.commit()


    def faker_vehicles(self, loop):
        status_provider = DynamicProvider(
            provider_name="status",
            elements=["available", "not available"]
        )
        make_provider = DynamicProvider(
            provider_name="make",
            elements=["Dodge", "Volkswagen", "Geo", "Volvo", "Acura", "Suzuki", "Rolls-Royce", "Mazda", "Chevrolet", "Porsche"]
        )
        model_provider = DynamicProvider(
            provider_name="model",
            elements=["Ram Van 2500", "Rabbit", "Tracker", "S70", "TL", "SX4", "Phantom", "B-Series", "Impala", "Boxster"]
        )

        fake = Faker()
        fake.add_provider(status_provider)
        fake.add_provider(make_provider)
        fake.add_provider(model_provider)
        for r in range(loop):
            self.cursor.execute(f"""INSERT INTO lyfter_car_rental.vehicles(make, model, manufacture_year, status)
                                VALUES (%s, %s, %s, %s)
            """,(
            fake.make(),
            fake.model(),
            fake.date(),
            fake.status()
            ))
        self.connection.commit()


    def faker_users_vehicles(self, minloop, maxloop):
        status_provider = DynamicProvider(
            provider_name="status",
            elements=["rent", "pending", "overdue", "in proccess"]
        )
        fake = Faker()
        fake.add_provider(status_provider)
        loop = random.randint(minloop, maxloop)
        for r in range(loop):
            self.cursor.execute(f"""INSERT INTO lyfter_car_rental.users_vehicles(user_id, vehicle_id, status)
                                VALUES (%s, %s, %s)
            """,(
            fake.unique.random_int(min=1, max= 250),
            fake.unique.random_int(min=1, max= 110),
            fake.status()
            ))
        self.connection.commit()