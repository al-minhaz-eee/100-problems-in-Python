"""
33.User will provide  2 numbers you have to find the by LCM of those 2
 numbers
"""
def find_hcf(a, b):
    while b:
        a, b = b, a%b
    return a
def find_lcm(a, b):
    lcm = abs(a*b)//find_hcf(a, b)
    return lcm

num1 = int(input("Enter first number "))
num2 = int(input("Enter last number "))
print(find_lcm(num1, num2))