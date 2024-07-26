"""
28.Write a program to print whether a given number is prime number or
 not
"""
def checking_prime(n):
    if n<=0 :
        return "Not prime"
    elif n== 2:
        return "prime"
    elif n%2==0:
        return "Not prime"
    for i in range(3,int(n**0.5)+1, 2):
        if n%i ==0:
            return "Not prime"
    return "Prime"

num = int(input("Enter a number to checking wheather prime or not, n = "))

print(f"{num} is {checking_prime(num)} number")
