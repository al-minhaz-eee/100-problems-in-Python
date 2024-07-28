"""
69.Write a program to replace an item with a different item if found in the
 list
"""
def replace(list, old, new):
    for idx, item in enumerate(list):
        if item == old:
            list[idx] = new
    return list

input_list = list(map(int, input("Enter list : ").split()))
s_item = int(input("Enter search item : "))
r_item = int(input("Enter replace item : "))
print(replace(input_list, s_item, r_item))

