CREATE TABLE lyfter_car_rental.users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        birthday TEXT NOT NULL,
        status VARCHAR(50) NOT NULL
        );


CREATE TABLE lyfter_car_rental.vehicles(
        id SERIAL PRIMARY KEY,
        make VARCHAR(50) NOT NULL,
        model VARCHAR(50) NOT NULL,
        manufacture_year TEXT NOT NULL,
        status VARCHAR(50) NOT NULL
        );


CREATE TABLE lyfter_car_rental.users_vehicles(
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        vehicle_id INT NOT NULL,
        rent_date DATE DEFAULT CURRENT_DATE,
        rent_status VARCHAR(50) NOT NULL
        );