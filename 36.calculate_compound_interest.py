"""
 36.Write a program to find the compound interest
"""
def Compound_interest(p, r, n, t):
    A = (p * (1 + r / (100 * n)) ** (n * t))
    CI = A - p
    return CI

p = float(input("Principle amount: "))
t = float(input("Period of interest "))
r = float(input("rate of interest: "))
n = float(input("time compounded: "))
CI = Compound_interest(p, r, n, t)
print(f"compound interest is {CI:.2f}")