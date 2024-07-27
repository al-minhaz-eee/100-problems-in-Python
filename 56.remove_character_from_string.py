"""
 56.Write a program which can remove a particular character from a string.
"""
def remove_char(string, character):
    return string.replace(character, '')


sen = input('Enter a sentence ')

ch = input('Enter a character ')

print(remove_char(sen, ch))

