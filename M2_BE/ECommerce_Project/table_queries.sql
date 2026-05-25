CREATE TABLE e_commerce.brand(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
        );


CREATE TABLE e_commerce.category(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL,
        description TEXT NOT NULL
        );


CREATE TABLE e_commerce.status(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL
        );


CREATE TABLE e_commerce.payment_method(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
        );


CREATE TABLE e_commerce.role(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
        );


CREATE TABLE e_commerce.user(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        username VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(250) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        role_id INT NOT NULL,
        FOREIGN KEY (role_id) REFERENCES e_commerce.role(id)
        );


CREATE TABLE e_commerce.product(
        id SERIAL PRIMARY KEY,
        sku VARCHAR(100) UNIQUE NOT NULL,
        name VARCHAR(100) NOT NULL,
        price INT NOT NULL,
        currency VARCHAR(100) NOT NULL,
        description TEXT NOT NULL,
        category_id INT NOT NULL,
        FOREIGN KEY (category_id) REFERENCES e_commerce.category(id),
        brand_id INT NOT NULL,
        FOREIGN KEY (brand_id) REFERENCES e_commerce.brand(id)
        );


CREATE TABLE e_commerce.store(
        id SERIAL PRIMARY KEY,
        product_id INT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES e_commerce.product(id),
        amount INT NOT NULL,
        date_of_admission DATE DEFAULT CURRENT_DATE,
        expiration_date DATE DEFAULT NULL,
        status_id INT NOT NULL,
        FOREIGN KEY (status_id) REFERENCES e_commerce.status(id)
        );


CREATE TABLE e_commerce.bill(
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES e_commerce.user(id),
        date_of_purchase DATE DEFAULT CURRENT_DATE,
        total_amount INT NOT NULL,
        currency VARCHAR(100) NOT NULL,
        payment_method_id INT NOT NULL,
        FOREIGN KEY (payment_method_id) REFERENCES e_commerce.payment_method(id)
        );


CREATE TABLE e_commerce.product_bill(
        id SERIAL PRIMARY KEY,
        product_id INT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES e_commerce.product(id),
        bill_id INT NOT NULL,
        FOREIGN KEY (bill_id) REFERENCES e_commerce.bill(id),
        product_amount INT NOT NULL,
        total_amount INT NOT NULL,
        currency VARCHAR(100)
        );


CREATE TABLE e_commerce.shopping_cart(
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES e_commerce.user(id)
        );


CREATE TABLE e_commerce.product_shopping_cart(
        id SERIAl PRIMARY KEY,
        shopping_cart_id INT NOT NULL,
        FOREIGN KEY (shopping_cart_id) REFERENCES e_commerce.shopping_cart(id),
        product_id INT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES e_commerce.product(id),
        product_amount INT NOT NULL
        )