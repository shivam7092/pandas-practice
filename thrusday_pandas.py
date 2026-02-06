import pandas as pd

print("===PANDAS CORE OPERATIONS ===\n")

data = {
    'name':['Alice','Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [70000, 65000, 80000, 72000, 68000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n" +"="*50 + "\n")

# ================================
#  1.filtering the data (like SQL Where)
# ================================


print("===FILTERING===\n")
# filter salary > 70000

high_salary = df[df['salary'] > 70000]
print("Employees with salary > 70000:")
print(high_salary)
print()

#filter: IT department only 

it_dept = df[df['department']=='IT']
print("Employees working in IT department:")
print(it_dept)
print()

#multiple conditions (AND) - use &

it_and_high = df[(df['department'] == 'IT') & (df['salary'] > 70000)]
print("Employees working in IT and have salary more then 70000")
print(it_and_high)
print()

#Multiple conditions (OR) - use |

young_or_rich = df[(df['age'] <= 30) | (df['salary'] > 70000)]
print("Employees who are younger then 30 OR earning mre then 70k")
print(young_or_rich)
print()

# ==========================================
# 2. SELECTING COLUMNS (like SQL SELECT)
# ==========================================

print("=== SELECTING COLUMNS ===\n")

#select one column
names = df['name']
print("just names:")
print(names)

#selecting multiple columns
name_Salary = df[['name','salary']]
print("name and salary")
print(name_Salary)
print()


# ==========================================
# 3. SORTING (like SQL ORDER BY)
# ==========================================

print("=== SORTING ===\n")

# Sorting ascending 
by_age = df.sort_values('age')
print("Sorted by age (low to high): ")
print(by_age)
print()

# sorting descending

by_salary = df.sort_values('salary', ascending=False)
print("Salary by salary(high to low) : ")
print(by_salary)
print()

# Sort by name alphabetically

name_sort = df.sort_values('name')
print(name_sort)
print()


# ==========================================
# 4. ADDING COLUMNS (NEW - Learn this now)
# ==========================================

print("\n ===ADDING COLUMNS ===\n")

#simple calculation

df['bonus'] = df['salary'] * 0.10
print("with bonus column: ")
print(df[['name', 'salary', 'bonus']])
print()

# conditional column

df['senior'] = df['age'] >= 30
print("with senior flag :")
print(df[['name','salary','bonus','age','senior']])
print()

#adding high earner column

df['high_earner'] = df['salary'] > 70000
print(" with Hiighest earner :")
print(df[['name','salary','high_earner']])
print()

# ==========================================
# 5. GROUPING (NEW - Most important!)
# ==========================================

print("\n ==== GROUPING ==== \n")

# Group by and calculate mean
avg_by_dept  = df.groupby('department')['salary'].mean()
print("Average salary by department: ")
print(avg_by_dept)
print()

# Count by group 

count_by_dept = df.groupby('department').size()
print("count by department : ")
print(count_by_dept)
print()

# calculate max salary by department

max_by_dept = df.groupby('department').max()
print("max salary by department : ")
print(max_by_dept)
print()


#===============================
#=========Excercise ============
#===============================


print("\n\n" + "="*60)
print("=== EXERCISES - MUST COMPLETE ===")
print("="*60 + "\n")

# Sample product data
products = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    'price': [1000, 25, 75, 400, 150, 80],
    'stock': [15, 50, 30, 12, 25, 35],
    'rating': [4.5, 4.0, 4.2, 4.7, 3.8, 4.1]
}

product_df = pd.DataFrame(products)
print("Product Data :")
print(product_df)
print()


# ==========================================
# EXERCISE 1: Filter expensive products
# ==========================================

# TODO: Filter products where price > 100
print("exercise 1: products with price > 100")

expensive = product_df[product_df['price'] > 100]
print("Below are the Expensive product :")
print(expensive)
print()

# ==========================================
# EXERCISE 2: Sort by rating
# ==========================================

# TODO: Sort by rating descending
print("Exercise 2: products sorted by the rating (best first)")

best_rated = product_df[product_df['rating'] > 4]
print("Below are the best rated products : ")
print(best_rated)
print()

# ==========================================
# EXERCISE 3: Add total_value column
# ==========================================

# TODO: Add column 'total_value' = price * stock

print("Excercise 3 : Calculate the inventory Value (price * stock)")

product_df['total_value'] = product_df['price'] * product_df['stock']
print("Total inventory value of the product :")
print(product_df[['product','price','stock','total_value']])
print()

# ==========================================
# EXERCISE 4: Group by category
# ==========================================

# TODO: Calculate average price per category

print("Exercise 4: Average price by category")

avg_price_by_category = product_df.groupby('category')['price'].mean()
print(avg_price_by_category)
print()

# ==========================================
# EXERCISE 5: Multiple operations
# ==========================================

# TODO: 
# 1. Filter: category == 'Electronics' AND price > 100
# 2. Sort by price descending
# 3. Select only: product, price, stock

print("EXERCISE 5: High-value electronics")

high_value_electronics = product_df[(product_df['category'] =='Electronics') & (product_df['price']>100) ]
print(high_value_electronics)

#Save as CSV
print("\n\n=== CSV FILES ===\n")

product_df.to_csv('products.csv', index = False) #csv file already saved

#Read from CSV

df_from_csv = pd.read_csv('products.csv')
print("\n Read from CSV:")
print(df_from_csv.head())
print()

# ==========================================
# EXERCISE 6: Real data analysis
# ==========================================

# Create sales data
sales_data = {
    'date': ['2024-02-01', '2024-02-01', '2024-02-02', '2024-02-02', '2024-02-03'],
    'product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Monitor'],
    'quantity': [2, 5, 1, 3, 1],
    'price': [1000, 25, 1000, 75, 400]
}

#creating sales data frame

sales_df = pd.DataFrame(sales_data)
print(sales_df)
print()

print("Calculation the total revenue (quantity * price)")

sales_df['revenue'] = sales_df['quantity'] * sales_df['price']
print(sales_df[['product','revenue']])
print()

# TODO: Find total revenue by product

revenue_by_product = sales_df.groupby('product')['revenue'].sum()
print(revenue_by_product)
print()

revenue_by_product.to_csv('sales_summary.csv', index = False)