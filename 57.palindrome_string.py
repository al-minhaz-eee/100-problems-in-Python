"""
 57.Write a program that can check whether a given string is palindrome or
 not.
"""

def is_palindrome(string):
    cleaned_string = string.replace(" ", '').lower()
    reverse = cleaned_string[::-1]
    return cleaned_string == reverse
sen = input("Enter string ")
if is_palindrome(sen):
    print("Palindrom ")
else:
    print("Not palindrome")