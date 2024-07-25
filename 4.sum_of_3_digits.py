# 4. Write a program that will give you the sum of 3 digits
n = int(input("Enter a number of 3 digits: "))
sum = 0
while n!=0:
     div = n%10
     print(div)
     n = n//10
     sum += div
     print(sum)
print("Sum of digits: ", sum)
