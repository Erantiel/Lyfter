-- Select all information from an specific user
SELECT *
FROM e_commerce.shopping_cart
WHERE user_id = 7
-- Select all bills from the same user
SELECT *
FROM e_commerce.bill
WHERE user_id =  2
-- Select all the products where that are related to the same bill
SELECT *
FROM e_commerce.product_bill
WHERE bill_id = 1