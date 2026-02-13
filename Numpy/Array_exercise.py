import numpy as np

#Valid Sudoku
# s = np.array([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])

# b = np.sum(s, axis=1)
# for i in b:
#     if i != 45:
#         print("Sudoku is not valid !")
# else:
#     print("Sudoku is valid for rows !")

# c = np.sum(s, axis=0)
# for i in c:
#     if i != 45:
#         print("Sudoku is not valid !")
# else:
#     print("Sudoku is valid for cols !")


# print(s[0:3,0:3])
# print("\n")
# print(s[0:3,3:6])
# print("\n")
# print(s[0:3,6:10])


# for i in range(0,9,3):
#     for j in range(0,9,3):
#         print(s[i:i+3, j:j+3])
#         n = s[i:i+3, j:j+3]
#         print(n.sum())
        


# Columns: [Age, Math Marks, Science Marks]
data = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])

#Get the shape of the matrix.
print(data.shape)
#Find the average age of students. -> For this we can use mean Fucntion
avg = np.mean(data[:, 0])
print(avg)
#Extract Math marks of all students.
extract = data[:, 1]
print(extract)
#Find the highest Science mark.
high = np.max(data[:,2])
print(high)
#Get details of the student who scored more than 90 in Math.
data1 = data[data[:, 1] > 90]
print(data1)

#Increase Math marks of all students by 5
# Columns: [Age, Math Marks, Science Marks]
data1 = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])
math = data1 + 5
print(math)


#Find how many students are younger than 19.
young =  data1[data1[:,0] < 19]
print(young)


#Calculate the average marks in each subject (column-wise mean).
avg1 = np.mean(data1[:,1:],axis=0)
print(avg1)


#Get data of students who scored at least 80 in both subjects.
data2 = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])
data2[(data2[:,1] >= 80) & (data2[:,2] >= 80)]
print(data2)



#Replace all Science marks < 75 with 0.
# Columns: [Age, Math Marks, Science Marks]
data3 = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])
data[:,2][data[:,2] < 75]= 0
print(data)