"""
 17. Write a program that will take three digits from the user and add
 the square of each digit.
"""
num = int(input("Enter a three digit number: "))
temp = num
sum =0
while temp!=0:
    remaider = temp%10
    remaider = remaider**2
    temp = temp//10
    sum +=remaider
print(f"square of digits of {num} is {sum}")