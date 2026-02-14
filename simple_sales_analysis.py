import pandas as pd

# Create data
sales = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse'] * 3,
    'quantity': [2, 5, 3, 1, 4, 2, 6, 1, 3, 8, 1, 2, 4, 3, 5],
    'price': [1000, 25, 75, 1000, 25, 1000, 25, 75, 1000, 25, 1000, 25, 75, 1000, 25]
})

print(sales)

# calculate revenue

sales['revenue'] = sales['quantity'] * sales['price']

# analysis

total_revenue = sales['revenue'].sum()
print(f"Total revenue : {total_revenue}")

print("\nBy Product:")

revenue_by_product = sales.groupby('product')['revenue'].sum()
print(f"revenue by Product: {revenue_by_product}")

print("\n>>> BONUS ANALYSIS")

# 1. Average transaction value
avg_transaction = sales['revenue'].mean()

print(f"\n Average Transaction : ${avg_transaction : ,.2f}")
print()

# 2. Top 3 products by quantity sold

top_qty = sales.groupby('product')['quantity'].sum().sort_values(ascending = False)
print(f"top qty: \n {top_qty}")

#save 
sales.to_csv('sales_analysis.csv', index = False)
print("\n saved results ")



