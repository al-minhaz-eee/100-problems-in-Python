"""
47. Write a Python Program to Find the Sum of the Series till the nth term:
 1 + x^2/2 + x^3/3 + …x^n/n
 n will be provided by the user
"""
import math
def sum_of_n(x, n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    else:
        return (x ** n) / n + sum_of_n(x, n - 1)

print("1 + x^2/2 + x^3/3 + … + x^n/n")

# Input from user
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))

# Calculate the sum of the series using the recursive function
result = sum_of_n(x, n)

# Output the result
print(f"Sum of the series 1 + x^2/2 + x^3/3 + … + x^n/n is: {result:.6f}")
