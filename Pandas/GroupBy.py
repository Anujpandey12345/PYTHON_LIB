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



import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Anuj", "Rahul", "Priya", "Neha", "Amit"],
    "Age": [23, 25, 22, 24, 26],
    "Marks": [78, 85, 67, 90, 88]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Calculate average marks
average_marks = df["Marks"].mean()
print("Average Marks:", average_marks)

# Filter students with marks greater than 80
top_students = df[df["Marks"] > 80]
print(top_students)
