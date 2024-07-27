"""
 48.The natural logarithm can be approximated by the following series.
 (x-1)/x + ((x-1)/x)^2/2 + ...+ ((x-1)/x)^n/2
 If x is input through the keyboard, write a program to calculate the
 sumofthe first seven terms of this series.
"""
def sum_of_term(x ,n=7):
    if n == 1:
        return ((x-1)/x)
    return 0.5*((x-1)/x)**n/2 + sum_of_term(x, (n-1))
x = float(input(" (x-1)/x + ((x-1)/x)^2/2 + ...+ ((x-1)/x)^n/n, where n=7, x = "))
print("sum of series x = ", sum_of_term(x))