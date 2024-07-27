"""
64.Write a program that can reverse words of a given string.
 Eg if the input is Hello how are you
 Output should be you are how Hello
"""
def revese_words(string):
    words = string.split()
    words.reverse()
    string = ' '.join(words)
    return string
input_strings = input("Enter strings : ")
print(revese_words(input_strings))