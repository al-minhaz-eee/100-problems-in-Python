"""44. Write a programtoprint the following pattern
 1
 1 2 1
 1 2 321
 1 2 34321
 1 2 3454321
 """
for i in range(5):
    for j in range(i+1):
        print(j+1, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()