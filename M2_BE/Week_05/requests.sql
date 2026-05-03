-- Tarea 2: Pruebas básicas de la DB
-- 1. Con la DB creada, cree los siguientes scripts de SQL:
INSERT INTO lyfter_car_rental.users(name, email, username, password, birthday, status) --a. Un script que agregue un usuario nuevo
    VALUES('Michael Mendoza', 'mmendoza@lyfter.com', 'mmendoz98', 'Hjkm1287Nm/','4/25/1995', 'active');
----------
INSERT INTO lyfter_car_rental.vehicles(make, model, manufacture_year, status) --b. Un script que agregue un automovil nuevo
    VALUES('Volvo', 'S80', '12/8/2015', 'available');
----------
UPDATE lyfter_car_rental.users SET --c. Un script que cambie el estado de un usuario
    status = 'disabled'
    WHERE id = 51;
----------
UPDATE lyfter_car_rental.vehicles SET --d. Un script que cambie el estado de un automovil
    status = 'not available'
    WHERE id = 11;
----------
INSERT INTO lyfter_car_rental.users_vehicles(user_id, vehicle_id, rent_status) --e. Un script que genere un alquiler nuevo con los datos de un usuario y un automovil
    VALUES(1,1,'rented');
UPDATE lyfter_car_rental.vehicles SET
    status = 'rented'
    WHERE id = 1;
INSERT INTO lyfter_car_rental.users_vehicles(user_id, vehicle_id, rent_status) -- More data for request 'g'
    VALUES(1,3,'rented');
UPDATE lyfter_car_rental.vehicles SET
    status = 'rented'
    WHERE id = 3;
INSERT INTO lyfter_car_rental.users_vehicles(user_id, vehicle_id, rent_status) -- More data for request 'g'
    VALUES(1,6,'rented');
UPDATE lyfter_car_rental.vehicles SET
    status = 'rented'
    WHERE id = 6;
----------
UPDATE lyfter_car_rental.users_vehicles SET --f. Un script que confirme la devolución del auto al completar el alquiler, colocando el auto como disponible y completando el estado del alquiler
    rent_status = 'premature completion'
    WHERE id = 1;
UPDATE lyfter_car_rental.users_vehicles SET
    rent_devolution_date = CURRENT_DATE
    WHERE id = 1;
UPDATE lyfter_car_rental.vehicles SET
    status = 'available'
    WHERE id = 1;
----------
UPDATE lyfter_car_rental.vehicles SET --g. Un script que deshabilite un automovil del alquiler
    status = 'not available'
    WHERE id = 1;
----------
SELECT * from lyfter_car_rental.vehicles -- h. Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.
    WHERE status LIKE 'rented';
SELECT * from lyfter_car_rental.vehicles
    WHERE status LIKE 'available';