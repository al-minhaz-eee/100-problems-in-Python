"""
 29.Print all the armstrong numbers in the range of 100 to 1000
"""
def is_armstrong(n):
    power_sum = sum(int(digit)**len(str(n)) for digit in str(n))
    return power_sum == n
def armstrong():
    for i in range(100, 1001):
        temp = i
        sum = 0
        while temp!=0:
            remainder = temp%10
            remainder = remainder**len(str(i))
            temp = temp//10
            sum +=remainder
        if(sum == i):
            yield i
a =armstrong()
print(f"armstrong number are in between 100 to 1000")
for num in a:
    print(num)
print(f"armstrong number are in between 100 to 1000")
for n in range(100, 1001):
    if is_armstrong(n) is True:
        print(n)