"""
 60.Write a python program to find the max item from a list without using
 the max function
"""
def max_in(list):
    max = list[0]
    for item in list:
        if item > max:
            max = item
    print(max)
list = [1, 2,4,43,34,23,4,5,53,5,23,23,32,2,12,3,4,56,746,4,64,6,47,31,234,1,36,57,31]
max_in(list)