"""
 45. Writeaprogramtoprint the following pattern
 1
 2 3
 4 5 6
 7 8 9 10
"""
k = 1
for i in range(5):
    for j in range(i):
        print( k, end="")
        k+=1
    print()
