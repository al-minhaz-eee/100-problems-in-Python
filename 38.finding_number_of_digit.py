"""
38.Take a number from the user and find the number of digits in it
"""
def find_digit(n):
    temp =n
    digits =[]
    while temp!=0:
        remainder = temp%10
        digits.append(remainder)
        temp = temp//10
    digits.reverse()
    no_digits =len(str(n))
    return digits,no_digits
n = int(input("Enter a number: "))
digits, no= find_digit(n)
print(f"{digits} and \n number of digits {no}")