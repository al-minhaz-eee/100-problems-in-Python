"""
 31. Write a program to print all the unique combinations of 1,2,3 and 4
"""
import itertools

numbers = [1, 2, 3, 4]

permutations = itertools.permutations(numbers)

print("All unique combinations of 1, 2, 3, and 4:")

for unique in permutations:
    print(unique)