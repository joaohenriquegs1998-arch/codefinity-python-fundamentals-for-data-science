# Initialize the lists
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# Function to calculate revenue
def calculate_revenue(prices, quantities_sold):
    revenue = []

    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])

    return revenue

# Function to sort and print the output
def formatted_output(revenues):
    revenues = sorted(revenues)  # Sort alphabetically by product name

    for product_name, revenue in revenues:
        print(f"{product_name} has total revenue of ${revenue:.2f}.")

# Calculate the revenue for each product
revenue = calculate_revenue(prices, quantities_sold)

# Combine products and revenues into a list of tuples
revenue_per_product = list(zip(products, revenue))

# Display the results
formatted_output(revenue_per_product)