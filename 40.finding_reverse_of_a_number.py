"""
40.Find the reverse of a number provided by the user(any number of digit)
"""
def reverse(n):
    temp =n
    reverse=""
    while temp!=0:
        remainder = temp%10
        reverse+=str(remainder)
        temp =temp//10
    return reverse
def easy_reverse(n):
    n = "".join(reversed(n))
    return n
def slicing_reverse(n):
    n = n[ : :-1]
    return n
n = int(input("Enter a number: "))
print(f"The reverse of {n} is {str(reverse(n))}")

n = input("Enter a number: ")
print(f"The reverse of {n} is {easy_reverse(n)}")

n = input("Enter a number: ")
print(f"The reverse of {n} is {slicing_reverse(n)}")