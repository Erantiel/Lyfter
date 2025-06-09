item_453_total_sale = 0.0
item_432_total_sale = 0.0
item_324_total_sale = 0.0
item_23_total_sale = 0.0

sales = [
	{
		"date": "27/02/23",
		"customer_email": "joe@gmail.com",
		"items": [
			{
				"name": "Lava Lamp",
				"upc": "ITEM-453",
				"unit_price": 65.76,
			},
			{
				"name": "Iron",
				"upc": "ITEM-324",
				"unit_price": 32.45,
			},
			{
				"name": "Basketball",
				"upc": "ITEM-432",
				"unit_price": 12.54,
			},
		],
	},
	{
		"date": "27/02/23",
		"customer_email": "david@gmail.com",
		"items": [
			{
				"name": "Lava Lamp",
				"upc": "ITEM-453",
				"unit_price": 65.76,
			},
			{
				"name": "Key Holder",
				"upc": "ITEM-23",
				"unit_price": 5.42,
			},
		],
	},
	{
		"date": "26/02/23",
		"customer_email": "amanda@gmail.com",
		"items": [
			{
				"name": "Key Holder",
				"upc": "ITEM-23",
				"unit_price": 3.42,
			},
			{
				"name": "Basketball",
				"upc": "ITEM-432",
				"unit_price": 17.54,
			},
		],
	},
]

for venta in sales:
    for producto in venta["items"]:
        upc = producto["upc"]
        precio = producto["unit_price"]
        if upc == "ITEM-453":
            item_453_total_sale = item_453_total_sale + precio
        elif upc == "ITEM-432":
            item_432_total_sale = item_432_total_sale + precio
        elif upc == "ITEM-324":
            item_324_total_sale = item_324_total_sale + precio
        elif upc == "ITEM-23":
            item_23_total_sale = item_23_total_sale + precio

print(item_453_total_sale)
print(item_324_total_sale)
print(item_432_total_sale)
print(item_23_total_sale)