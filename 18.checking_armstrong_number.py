"""
 18. Write a program that will check whether the number is armstrong
 number or not
"""

num = int(input("Enter a number: "))

temp = num
sum=0
while temp!=0:
    remainder = temp%10
    remainder = remainder**3
    temp = temp//10
    sum += remainder
print(f"Sum of Cube of every digits of{num} is {sum}")
if sum == num:
    print(num, " is armstrong")
else:
    print(num, "is not armstrong number")