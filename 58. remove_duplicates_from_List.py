"""
58.Write a python program to remove all the duplicates from a list
"""
def remove_duplicates(list):
    seen = set()
    unique_list = []
    for item in list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
list = [1,2,4,43,34,23,4,5,53,5,23,23,32,2,12,3,4,56,746,4,64,6,47,31,234,1,36,57,31]
print(remove_duplicates(list))