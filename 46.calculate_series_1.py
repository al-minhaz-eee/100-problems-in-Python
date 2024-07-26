"""
 46. Write a programtocalculate the sum of the following series till the
 nth term
 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
 nwill be provided by the user
"""
def sum_of_(n):
    if n==0:
        return 0
    return n/fact(n)+sum_of_series((n-1))
def sum_of_series(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i/fact(i)
    return sum
def fact(n):
    if n==1 or n ==0:
        return 1
    return n*fact(n-1)
n = int(input('1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!, n =' ))
print(f"sum of series is without recursion  ", sum_of_series(n))

n = int(input('1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!, n =' ))
print(f"sum of series is with recursion  ", sum_of_(n))