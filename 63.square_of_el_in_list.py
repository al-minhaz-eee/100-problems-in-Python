"""
3.Write a program that can create a new list from a given list where each
 item in the new list is square of the item of the old list
"""
import math
def square_of(list):
    return [item**2 for item in list]
input_list = list(map(int, input("Enter elements by space ").split()))
print(f"New list is {square_of(input_list)}")
