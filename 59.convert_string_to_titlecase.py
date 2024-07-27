"""
59.Write a python program to convert a string to title case without using
 the title()
"""
def title_string(string):
    words = string.split()
    title_case =[word[0].upper()+word[1:].lower() if word else " " for word in words]
    return ' '.join(title_case)
str = input("Enter your string ")
print(title_string(str))