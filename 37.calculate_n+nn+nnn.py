"""
37.Write a Python program that accepts an integer (n) and computes the
 value of n+nn+nnn
"""
def calculate(n):
    n1 = int(f"{n}")
    n2 = int(f"{n}{n}")
    n3= int(f"{n}{n}{n} ")
    return n1+ n2+ n3

n = int(input("Enter n = "))
print(f"{n}+{n}{n}+{n}{n}{n}  = {calculate(n)}")