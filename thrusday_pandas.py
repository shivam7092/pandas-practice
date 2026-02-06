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