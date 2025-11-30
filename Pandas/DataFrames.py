import pandas as pd
import numpy as np
# Using Dict
# data = {
#     'Name': ['Anuj', 'Arbaz', 'Pukar'],
#     'Age' : [22, 21, 21],
#     'City' : ['Kanpur', 'Sitapur', 'Danabd'],
#     'Salary' : [21000, 20000, 900000]
# }
# df = pd.DataFrame(data)
# print(df)
# We can also Use List for Creating DataFrames
Data_list = [
    ['Rohan', 25, 'Pune', 75000],
    ['Meera', 23, 'Delhi', 68000],
    ['Krish', 27, 'Delhi', 92000],
    ['Aisha', 23, 'Mumbai', 81000],
    ['Shyam', 24, 'Hyderabad', 70000]
]
df = pd.DataFrame(Data_list, columns=['Name', 'Age', 'City', 'Salary'])
# print(df)

# # Select and Indexing of Columns ..
# index_col = df['Name'] # We can see for Accessing index we need the name of Columns in DataFrames
# print(index_col)
# index_col1 = df[['Name','City']] # we Want two and More Columns 
# print(index_col1)

# # Create a New Columns in you Existing table 
# df['Designation'] = ['Eng.', 'Doctor', 'Asso Eng.', 'Bussiness man', 'ShopKeeper']
# print(df)


# #Remove A Column From you DataFrame
# remove = df.drop('Salary', axis=1, inplace=True) #Inplace Remove Columns Permanently
# print(remove)
# print(df)



# #Selecting the Rows- > loc() using this Fuction
# row = df.loc[0] # For One ROw
# print(row)
# print("\n")
# row1 = df.loc[[0,1,2]] #For Multiple Rows
# print(row1)
# row2 = df.iloc[[3,4]] # iloc() stand for index location some time we get diffrent index so we can use this 
# print(row2)



# Selection Subset of ROws and Columns ..........

# subset = df.loc[[0,1]][['City', 'Salary']] # First list of list for Rows and second liist of list for Columns 
# print(subset)

# print("\n")


con = df[df["Age"] > 22] # Only For One condition
print(con)
print("\n")
con1 = df[(df["Age"] > 22) &(df["City"] == "Delhi")] # For two condition and always use () parantheses
print(con1)