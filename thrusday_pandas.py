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