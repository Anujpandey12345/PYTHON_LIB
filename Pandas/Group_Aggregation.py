import pandas as pd
import numpy  as np
data = {
    'Category' : ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store' : ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales' : [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity' : [10, 15, 12, 18, 8, 20, 15, 25],
    'Date' : pd.date_range('2023-01-01', periods = 8)
}

df = pd.DataFrame(data)
print(df)

"""Group By"""
# 1. -> Group by Category and Calculate the sum of sales
cat = df.groupby('Category')
print(cat) # this Only create the Object you can't see this object
for i, v in cat: # If You want to see this Object then you need For loop
    print(i)
    print(v)

# For Calculating the sum 
cat = df.groupby('Category')['Sales'].sum()
print(cat)



# 2. -> Group by store and calculte the sum slaes

store = df.groupby('Store')['Sales'].sum()
print(store)


# 3. -> Group by Multiple Columns , Group by Category and store
storeCat = df.groupby(['Category','Store'])['Sales'].sum()
print(storeCat)



""""Aggregation"""

# Aggregation Function are - > mean, mode, median, std, min, max, count
aggg = df['Sales'].agg(['sum', 'mean', 'median', 'min', 'max', 'count', 'std'])  #We can't use mode with the .agg
print(aggg)