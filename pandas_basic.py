import pandas as pd

print('===PANDAS LEVEL 2===')

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [70000, 65000, 80000, 72000, 68000]
}

df = pd.DataFrame(data)
print(df)
print()

# Review: Selecting columns

print("=== SELECTING COLUMNS ===")
names  = df['name'] #single column
print("Just names :")
print(names)
print()

# ==========================================
# NEW: FILTERING (like SQL WHERE)
# ==========================================


print("="*50)
print('FILTERING')
print("="*50)

#filter by number
print("people with salary more then 70000: ")
high_salary = df[df['salary'] > 70000]
print(high_salary)
print()

#filter by text
print(" Only IT department: ")
it_dept = df[df['department'] == 'IT']
print(it_dept)
print()

# Filter with AND (&)

print("IT Department AND salary > 70k")
it_High = df[(df['department'] == 'IT') & (df['salary'] > 70000)]
print(it_High)
print()

# filter with OR (|)

print("Age <30 OR Salary > 75000: ")
young_and_rich = df[(df['age'] < 30) | (df['salary'] > 75000)]
print(young_and_rich)
print()

#practice

print("filter people age more the >= 30")
age_30_plus = df[df['age'] >= 30]
print(age_30_plus)
print()

# ==========================================
# NEW: SORTING (like SQL ORDER BY)
# ==========================================

print("="*50)
print(">>> NEW: SORTING")
print("="*50)
print()

# Group and calculate average

print("Average salary by department: ")
avg_by_dept = df.groupby('department')['salary'].mean()
print(avg_by_dept)
print()

# Group and count
print("count people per department: ")
count_by_dept = df.groupby('department').size()
print(count_by_dept)
print()

# Group and SUM
print(" Total Salary per Department: ")
total_by_dept = df.groupby('department')['salary'].sum()
print(total_by_dept)
print()

#practice 2
print("Try: Find max salary per department")
max_by_dept = df.groupby('department')['salary'].max()
print(max_by_dept)
print()

# ==========================================
# PRACTICE: Combine everything
# ==========================================

print("="*50)
print(">>> PRACTICE: Combining concepts")
print("="*50)
print()

# Example: Filter IT dept, sort by salary

it_sorted = df[df['department'] == 'IT'].sort_values('salary', ascending = False)
print("IT department sorted by salary: ")
print(it_sorted)
print()


print("\n\n=== EXERCISES ===\n")


