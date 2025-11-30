import pandas as pd
import numpy as np
# First we create all the DataType , Dataitems
labels = ['a', 'b', 'c', 'd', 'e']
arr = np.array([10, 20, 30, 40, 50])
my_list = [30, 40, 50, 60, 70]
my_dict = {1:20, 2:30, 3:40, 4:90, 5:100} # Keys are numbers
my_dictC = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50} #Keys are char

print(pd.Series(arr))
print(pd.Series(my_list))
print(pd.Series(my_list, index=labels)) # we can change the Labels(Index)
print(pd.Series(my_list, index=['o', 'q', 'a', 'h', 'f'])) # we can change the Labels(Index) means we can put inside the index


# Now dictonary
print(pd.Series(my_dict))  # In dict key are lables so we didn't need to name indexs
print(pd.Series(my_dictC)) # Lables are based on the key



