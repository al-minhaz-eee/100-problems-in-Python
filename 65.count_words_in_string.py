"""
65.Write a program that can count the number of words in a given string
"""
def count_words(string):
    return len(string.split())
input_strings = input("Enter strings : ")
print(count_words(input_strings))
