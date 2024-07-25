"""
 9. Write a program that take a user inputr of three angles and will
 find out whether it can form a triangle or not.
"""
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

if angle1+angle2+angle3 == 180:
    print("These angles form a triangle ")
else:
    print("These angles don't form a triangle")