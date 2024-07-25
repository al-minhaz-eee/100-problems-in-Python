"""
 13. Write a program that will tell whether the given number is divisible
 by 3&6.
"""
num = int(input("Enter a integer number: "))

if num%3 == 0 and num%6 == 0:
    print(f"{num} is divisible by 3 & 6")
elif num%3 == 0:
    print(f"{num} is divisible by 3 only")
else:
    print(f"{num} is not divisble by 3 or 6 or both")