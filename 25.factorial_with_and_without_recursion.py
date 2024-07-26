"""
 26.Write a program that can find the factorial of a given number provided
 by the user.
"""
def fact(n):
    if n<0 :
        return
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
def factorial(n):
    if n<0 :
        return
    if n==1 or n==0:
        return 1
    fact = 1
    for i in range(1, 1+n):
        fact *=i
    return fact
num = int(input("Enter a number to find factorial using recursion "))
print(f"factorial of {num} is {fact(num)} ")
num = int(input("Enter a number to find factorial without using recursion "))
print(f"factorial of {num} is {factorial(num)} ")
