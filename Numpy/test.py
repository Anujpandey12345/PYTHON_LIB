
with open("app.log", "r") as file:
    error = 0
    for line in file:
        if "ERROR" in line:
            print(line.strip())
            error += 1
print("num of error : ", error)





