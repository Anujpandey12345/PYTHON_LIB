list = [1, 1, 3, 5, 2, 2]
cout = {}
for i in list:
    if i in cout:
        cout[i] += 1
    else:
        cout[i] = 1
print(cout)


x = 10
sqr = lambda x : x * x
print(sqr)    



# SELECT DISTINCT salary
# FROM emp
# WHERE salary <> 10000 
# ORDER BY salary DESC
# LIMIT 1 OFFSET (N - 1);





