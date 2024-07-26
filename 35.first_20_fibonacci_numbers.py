"""
35.Print the first 20 numbers of a Fibonacci series
"""
def fibonacci(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1]+series[-2])
    return series
n = 20

series = fibonacci(n)
print("Fibonacci series of first 20 numbers are: ")
print(series)