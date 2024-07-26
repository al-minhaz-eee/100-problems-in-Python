"""
 24.Write a program to find the sum of first n numbers, where n will be
 provided by the user. Eg if the user provides n=10 the output should be
 55.
"""

def sum_upto_n(n):
    if n>=0:
        return n*(n+1)/2
n = int(input("Enter first upto n, n = "))
print(f"sum up to {n} is {sum_upto_n(n)}")