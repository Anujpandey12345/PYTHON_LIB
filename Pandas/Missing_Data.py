import pandas as pd
import numpy as np

# Find The Missing data..
data = {
    "A": [1, 2, 3, 4, np.nan], #np.nan for None data
    "B": [np.nan, 2, 3, 4, np.nan],
    "C": [1, 2, 3, np.nan, np.nan],
    "D": [1, 2, np.nan, 4, np.nan],
    "E": [1, np.nan, np.nan, np.nan, 5]
}
df = pd.DataFrame(data)
print(df)

#Fuction to  finding the nan data
print(df.isna())
print(df.sum()) # Give you some of rows number'
print(df.isna().sum()) # this gives you how much NAN available in each row 
print(df.isna().any()) # this give you that nan is avaiblae in all row if available then return true  , if not available then return  false

# #Remove 
# print(df.dropna())
# print(df.dropna(thresh=3))


#Filling Data
values = {"A":100, "B":3, "C":900, "D":77, "E":98}
print(df.fillna(value=values))
print(df.fillna(0, inplace=True)) #fill Zero in Each nan
print(df.fillna(df.mean()))  #Fill Avg 
print(df.fillna(df.mean()))