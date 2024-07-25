# User will input (3ages).Find the oldest one

a = int(input("Enter three ages: "))
b = int(input("Enter three ages: "))
c = int(input("Enter three ages: "))

if a>b and a>c :
    print(a,"is oldest among",a, b, c)
elif b>a and b>c:
    print(c, "is oldest among", a, b, c)
else:
    print(c, "is oldest among", a, b, c)