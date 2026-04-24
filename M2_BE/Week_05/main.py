from database import PgManager


database = PgManager("localhost", 5432, "postgres", "postgres", "postgres", "-c search_path=lyfter_car_rental") #Database created and connection made


database.close_connection() #Closes connection and cursor