"""
 61. Write a python program to reverse a list
"""
def reverse_list(list):
    return list[::-1]
lst = list(input("Enter numbers: ").split(" "))
print(reverse_list(lst))