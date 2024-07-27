"""
51. Find the length of a given string without using the len() function.
"""
def length(string):
    k=0
    for i in string:
        k+=1
        continue
    return k
sen = input("Enter a string: ")
print(length(sen))
