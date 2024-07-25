"""
19. Write a program that will take user input of (4 digits number) and
 check whether the number is narcissist number or not.
"""
num = int(input("Enter a number: "))
n = len(str(num))
temp = num
sum=0
while temp!=0:
    remainder = temp%10
    remainder = remainder**n
    temp = temp//10
    sum += remainder
print(f"Sum of raise to the power of {n} of every digits of{num} is {sum}")
if sum == num :
    print(num, " is narcissist")
else:
    print(num, "is not narcissist number")