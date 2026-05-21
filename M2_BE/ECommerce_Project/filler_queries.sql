--INSERT of Brands
INSERT INTO e_commerce.brand (name) VALUES ('Royal Canin');
INSERT INTO e_commerce.brand (name) VALUES ('Hills Science Diet');
INSERT INTO e_commerce.brand (name) VALUES ('Purina Pro Plan');
INSERT INTO e_commerce.brand (name) VALUES ('NutriSource');
INSERT INTO e_commerce.brand (name) VALUES ('Taste of the Wild');
--INSERT of Categories
INSERT INTO e_commerce.category (name, description) VALUES ('Food', 'Grocery items based on biological origins or nutritional properties');
INSERT INTO e_commerce.category (name, description) VALUES ('Dog Collars, Leashes & Harnesses', 'Travel, Walking, & Training section');
INSERT INTO e_commerce.category (name, description) VALUES ('Toys', 'Plush, Chew, Dental, Interactive, and Fetch/Tug');
INSERT INTO e_commerce.category (name, description) VALUES ('Miscellaneous', 'Random, overlapping, or specialty goods');
--INSERT of Status
INSERT INTO e_commerce.status (name) VALUES ('Available');
INSERT INTO e_commerce.status (name) VALUES ('Exhausted');
INSERT INTO e_commerce.status (name) VALUES ('Expired');
INSERT INTO e_commerce.status (name) VALUES ('Low Stockpile');
--INSERT of Payment Method
INSERT INTO e_commerce.payment_method (name) VALUES ('SINPE');
INSERT INTO e_commerce.payment_method (name) VALUES ('SINPE Movil');
--INSERT of Role
INSERT INTO e_commerce.role (name) VALUES ('Administrator');
INSERT INTO e_commerce.role (name) VALUES ('Client');
--INSERT of User
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Osias Alfaro', 'oalfaro', 'qB8,Grg)Qrrwr{', 'oalfaro@gmail.com', 1);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Giffy Kyberd', 'gkyberd0', 'qB8,Grg)Qrrwr{', 'gkyberd0@nbcnews.com', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Webster Battersby', 'wbattersby1', 'pB0_+)CZeZ8/ZB>z', 'wbattersby1@1und1.de', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Jeniffer Varfolomeev', 'jvarfolomeev2', 'vU6.hMs<V)Xl%PWh', 'jvarfolomeev2@shinystat.com', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Washington Louw', 'wlouw3', 'dU4#KGp(`CU.QpEk', 'wlouw3@illinois.edu', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Lincoln Shalloo', 'lshalloo4', 'pH2<|tmV', 'lshalloo4@biblegateway.com', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Talya Bompas', 'tbompas5', 'sH4,oe2@', 'tbompas5@comcast.net', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Addi Iapico', 'aiapico6', 'hG5=mYa"kH', 'aiapico6@artisteer.com', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Benoite Filintsev', 'bfilintsev7', 'kL4{f2YCXqOI', 'bfilintsev7@princeton.edu', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Milicent Dommersen', 'mdommersen8', 'eM0\4`KHYLb', 'mdommersen8@sourceforge.net', 2);
INSERT INTO e_commerce.user (name, username, password, email, role_id) VALUES ('Amalee Gilfether', 'agilfether9', 'yJ9~ZME!*', 'agilfether9@ftc.gov', 2);
--INSERT of Product
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('043310980', 'Dog Dry Food', '$20', '1KG', 1, 3);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('031100490', 'Dog Treats', '$7', '150G', 1, 1);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('081006052', 'Cat Dry Food', '$18', '1KG', 1, 2);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('042104469', 'Cat Treats', '$7', '150G', 1, 2);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('092900956', 'Dog Harness', '$15', 'Adjustable', 2, 4);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('081501175', 'Cat Harness', '$12', 'Adjustable', 2, 5);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('031275998', 'Bone Plush', '$15', 'Wool Made', 3, 1);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('061192753', 'Fish Plush', '$10', 'Wool Made', 3, 3);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('051408923', 'Bowl', '$20', 'Stainless Steel', 4, 4);
INSERT INTO e_commerce.product (sku, name, price, description, category_id, brand_id) VALUES ('111906161', 'Scratching Post', '$35', 'Non Toxic Sisal', 4, 5);
--INSERT of Store
INSERT INTO e_commerce.store (product_id, amount, expiration_date, status_id) VALUES (1, 30, '2026-7-19', 1);
INSERT INTO e_commerce.store (product_id, amount, status_id) VALUES (2, 0, 2);
INSERT INTO e_commerce.store (product_id, amount, expiration_date, status_id) VALUES (3, 15, '2026-2-1', 3);
INSERT INTO e_commerce.store (product_id, amount, expiration_date, status_id) VALUES (4, 5, '2026-8-23', 4);
INSERT INTO e_commerce.store (product_id, amount, status_id) VALUES (5, 10, 1);
INSERT INTO e_commerce.store (product_id, amount, status_id) VALUES (6, 12, 1);
INSERT INTO e_commerce.store (product_id, amount, status_id) VALUES (7, 5, 4);
INSERT INTO e_commerce.store (product_id, amount, status_id) VALUES (8, 3, 4);
INSERT INTO e_commerce.store (product_id, amount, status_id) VALUES (9, 13, 1);
INSERT INTO e_commerce.store (product_id, amount, status_id) VALUES (10, 6, 1);
--INSERT of Bill
INSERT INTO e_commerce.bill (user_id, total_amount) VALUES (2, '$67');
INSERT INTO e_commerce.bill (user_id, total_amount) VALUES (2, '$85');
INSERT INTO e_commerce.bill (user_id, total_amount) VALUES (7, '$100');
--INSERT of Product_Bill
INSERT INTO e_commerce.product_bill (product_id, bill_id, product_amount, total_amount) VALUES (1, 1, 3, '$60');
INSERT INTO e_commerce.product_bill (product_id, bill_id, product_amount, total_amount) VALUES (4, 1, 1, '$7');
INSERT INTO e_commerce.product_bill (product_id, bill_id, product_amount, total_amount) VALUES (5, 2, 1, '$15');
INSERT INTO e_commerce.product_bill (product_id, bill_id, product_amount, total_amount) VALUES (10, 2, 2, '$70');
INSERT INTO e_commerce.product_bill (product_id, bill_id, product_amount, total_amount) VALUES (9, 3, 2, '$40');
INSERT INTO e_commerce.product_bill (product_id, bill_id, product_amount, total_amount) VALUES (7, 3, 4, '$60');
--INSERT of Shopping Cart
INSERT INTO e_commerce.shopping_cart (id, user_id, product_id, product_amount, payment_method_id) VALUES (1, 7, 1, 2, 2);
INSERT INTO e_commerce.shopping_cart (id, user_id, product_id, product_amount, payment_method_id) VALUES (1, 7, 4, 1, 2);
INSERT INTO e_commerce.shopping_cart (id, user_id, product_id, product_amount, payment_method_id) VALUES (1, 8, 1, 5, 2);