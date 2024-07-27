"""
 49. Write a program that keeps on accepting a number from the user until
 the user enters Zero. Display the sum and average of all the numbers.
"""

sum = 0
total_num =0
while True:
    print("\n Enter a number: ")
    n = int(input(" n = "))
    if n ==0:
        break
    total_num += 1
    sum+=n
print("The sum of all number you entered is ", sum, " and Average is ", sum/total_num)