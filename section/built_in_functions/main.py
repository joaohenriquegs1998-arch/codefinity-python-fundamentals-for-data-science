# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
products = {
    "Apple": ["1.20", "50"],   # [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

total_sales_list = []

# Process each product
for product, values in products.items():
    price = float(values[0])
    quantity = int(values[1])

    total_sales = price * quantity
    total_sales_list.append(total_sales)

    print(f"Total sales for {product}: ${total_sales:.2f}")

# Summary statistics
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${total_sum:.2f}")
print(f"Minimum sales: ${min_sales:.2f}")
print(f"Maximum sales: ${max_sales:.2f}")
