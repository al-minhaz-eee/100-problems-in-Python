"""
7. Write a program that will tell whether the given year is a leap year
 or not
"""
year = int(input("Enter a valid year: "))

if year%400 ==0 and year%100 ==0:
    print("{0} is leap year".format(year))
elif year%4==0 and year%100 !=0:
    print("{0} is leap year".format(year))
else:
    print("{0} is not leap year".format(year))