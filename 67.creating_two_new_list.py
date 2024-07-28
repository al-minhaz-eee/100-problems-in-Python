"""
 67.Create 2 lists from a given list where 1st list will contain all the odd
 numbers from the original list and the 2nd one will contain all the even
 numbers
"""

def new_even(list):
    return [item for item in list  if item%2 == 0]
def new_odd(list):
    return [item for item in list  if item%2!=0]

input_list = list(map(int, input("Enter strings : ").split()))

print(f"even {new_even(input_list)}")
print(f"odd {new_odd(input_list)}")