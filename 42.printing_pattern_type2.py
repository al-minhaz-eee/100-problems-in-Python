"""
Write a program to print the following pattern
 *
 **
 ***
 **
 *
"""
n = 3
for i in range(0, 5):
    if i<=2:
        num_stars = i
    elif i>2:
        num_stars = 4 -i
    for j in range(num_stars+1):
        print("* ", end="")
    print()