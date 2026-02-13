"""In this , We will Learn some Operations in Pandas"""

# 1. -> DataFrame Basic Operations
import pandas as pd
import numpy as np
df1 = pd.DataFrame({
    'A' : [1, 2, 3, 4],
    'B' : [10, 20, 30, 40],
    'C' : [100, 200, 300, 400]
})
# print(df1)

# sp = df1.shape
# print(sp)
# cl = df1.columns
# print(cl)
# in1 = df1.info()
# print(in1)
# des = df1.describe()
# print(des)
# # Add data in perticuler column
# print(df1['A'] + 10)



# 2. -> DataFrames Applying Functions 

def square(x):
    return x**2

df1["B"] = df1["B"].apply(square)
print(df1)
df1["D"] = df1["B"].apply(square) # Create New Column
print(df1)
#By using Lambda
df1["E"] = df1["B"].apply(lambda x : x**2)
print(df1)