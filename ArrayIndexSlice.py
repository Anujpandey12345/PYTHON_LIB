import numpy as np



# #Multi-D
# arr = np.arange(1, 31).reshape(6, 5)
# # print(arr)
# # print(arr[0]) # this Only access the rows
# print(arr)

# # print(arr[0,0])
# # print(arr[4,2])
# # print(arr[3,2])



# #Slicing..
# print("\n")
# arr_slic = arr[3:6, 3:5]
# print(arr_slic)


#Boolean Indexing 
arr = np.arange(11, 21)
bool_index = arr % 2 == 0
print(bool_index)
arr = arr[bool_index]
print(arr)