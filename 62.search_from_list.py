"""
62.Write a python program to search a given number from a list
"""
def search_idx(list, element):
    for idx,item in enumerate(list):
        if item == element:
            return idx
    return -1
input_list = list(map(int, input("Enter the list of numbers separated by space: ").split()))
number_to_find = int(input("Enter the number to search for: "))
index = search_idx(input_list, number_to_find)
if index!=-1:
    print(f"Number found ar index {index}")
else:
    print(f"Number is not found")