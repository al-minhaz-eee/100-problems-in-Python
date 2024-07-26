"""
25.Write a program that can multiply 2 numbers provided by the user
 without using the * operator
"""
def multiply_without_sign(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    if b<0:
        result = - result
    return result

a = int(input("Enter first number "))
b = int(input("Enter second number "))

print(f"Multiply withou using * is {multiply_without_sign(a, b)}")
