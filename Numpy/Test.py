store_inventory = {
    "Bangalore": [0, 0, 1, 2, 2, 4, 4],
    "Delhi": [1, 1, 2, 2, 4],
    "Mumbai": [0, 2, 2, 3, 4, 4]
}
 
fruit_map = [
    [0, "apple"],
    [1, "banana"],
    [2, "orange"],
    [3, "grapes"],
    [4, "mango"]
]

all_member = store_inventory["Bangalore"] + store_inventory["Delhi"] + store_inventory["Mumbai"]
win = max(set(all_member), key=all_member.count)


for item in fruit_map:
    if item[0] == win:
        print("the winner is : ", item[1])
        print(item)