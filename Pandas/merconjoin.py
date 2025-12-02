# In this Chapter we are learn about Merging, joining, Conca etc


# 1. Merging -> First we Create two DataFrame

import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "employee_id":  [1, 2, 3, 4],
    "name" : ["Anuj", "Arbaz", "Ankit", "Pukar"],
    "department " : ["IT", "Civil", "Machanical", "Electrical"]
})
salary = pd.DataFrame({
    "employee_id" : [1, 2, 3, 7], 
    "salry" : [9000, 8000, 7000, 10000],
    "bonus" : [100, 300, 500 , 200]
})




p1 = pd.merge(employees, salary, on="employee_id", how="inner") # only common value 
p2 = pd.merge(employees, salary, on="employee_id", how="outer") # Common + Without common
p3 = pd.merge(employees, salary, on="employee_id", how="left") #merge on basis of Emp
p4 = pd.merge(employees, salary, on="employee_id", how="right") #merge on basis of Salry

# print(p1)
print(p2)
# print(p3)
# print(p4)
