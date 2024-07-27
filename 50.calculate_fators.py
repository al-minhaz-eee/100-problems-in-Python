"""
 50.Write a program that accepts 2 numbers from the user a numerator
 and a denominator and then simplifies it
 Eg if the num =5, den=15theanswershould be ⅓
 Eg if the num =6, den=9theanswershouldbe⅔
"""
import math
def simplified_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)

    numerator = numerator//gcd
    denominator = denominator//gcd
    return numerator, denominator

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

n,m = simplified_fraction(numerator, denominator)

print(f"The simplified fraction is {n}\\{m}")