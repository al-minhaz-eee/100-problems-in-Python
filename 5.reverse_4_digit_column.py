"""5. Write a program that will reverse a four digit number.Also it checks
 whether the reverse is true."""

n = int(input("Enter a number of 4 digits: "))
temp = n
rev = 0
while temp!=0:
     div = temp%10
     temp = temp//10
     rev = rev*10+div

print("reverse of digits of ",n, " is ", rev)

print("checking reverse is the original or not")
if rev == n:
    print("True")
else:
    print("False, You have reversed the ", n)