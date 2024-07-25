# 4. Write a program that will give you the sum of 3 digits of user input
n = int(input("Enter a number of 3 digits: "))
sum = 0
while n!=0:
     div = n%10
     n = n//10
     sum += div
print("Sum of digits: ", sum)

