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


