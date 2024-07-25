"""
 11. Write a program to find the simple interest when the value of
 principle,rate of interest and time period is given.
"""
p = float(input("Enter principle amount: "))
r = float(input("Enter rate of interest: "))
n = float(input("Enter time period in years: "))

I = p*r*n/100
print(f"Simple interest is {I}")