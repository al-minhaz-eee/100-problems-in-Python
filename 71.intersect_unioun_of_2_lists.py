"""
 71. Write a program that can perform union and intersection on 2 given list.
"""
def unioun_(list1, list2):
    return list(set(list1) | set(list2))
def intersect_(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(f'Unioun of {list1} and {list2} is {unioun_(list1, list2)}')
print(f'intersect of {list1} and {list2} is {intersect_(list1, list2)}')
