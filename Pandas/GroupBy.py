import pandas as pd

# Sample DataFrame
data = {
    "name": ["Amit", "Neha", "Ravi", "Pooja", "Kiran"],
    "department": ["IT", "HR", "IT", "HR", "Finance"],
    "salary": [50000, 40000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

# Group by department and calculate average salary
avg_salary = df.groupby("department")["salary"].mean()

print(avg_salary)
