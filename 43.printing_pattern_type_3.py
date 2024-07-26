"""
 43.Write a program to print the following pattern
 *
 * * *
 * * * **
 * * * ****
 * * * ******
"""
for i in range(5):
    for k in range(5-i):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
