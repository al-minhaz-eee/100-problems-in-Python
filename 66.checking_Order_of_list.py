"""
 66.Write a program to check if a list is in ascending order or not
"""
def is_accending(list):
    for i in range(len(list)-1):
        if list[i]>=list[i+1]:
            return False
    return True

input_list = list(map(int, input("Enter strings : ").split()))
if is_accending(input_list):
    print("list is in accending order")
else:
    print("list is not in accending order")
