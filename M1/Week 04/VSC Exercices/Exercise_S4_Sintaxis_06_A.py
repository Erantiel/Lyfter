price = int(input("Enter the price of the product: "))

if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10

print(f'The price of the product with the discount is: {price - discount}')