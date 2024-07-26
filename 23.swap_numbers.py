"""
 23.Write a program that will swap numbers
"""
def swap_numbers(a, b):
    temp = a
    a =b
    b = temp
    return a, b
def swap_numbers_pythonic(a, b):
    a, b = b, a
    return a, b
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

swaped_num1, swaped_num2 = swap_numbers(num1, num2)
print(f"swaping using temp variable are {swaped_num1, swaped_num2}")

swaped_num1, swaped_num2 = swap_numbers_pythonic(num1, num2)

print(f"pythonic swapings are {swaped_num1, swaped_num2}")
