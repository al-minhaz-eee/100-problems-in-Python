"""
 39.Print all factors of a given number provided by the user.
"""
n = int(input("Enter a number: "))
print(list(filter(lambda i:  n%i ==0, range(1, n+1))))