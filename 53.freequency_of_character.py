"""
 53.Count the frequency of a particular character in a provided string. Eg
 'hello how are you' is the string, the frequency of h in this string is 2.
"""
def count_characer(string, ch):
    count=0
    for char in string:
        if char == ch:
            count+=1
    return count

sen = input('Enter a sentence ')
ch = input('Enter a character for frequency calculate')
print(count_characer(sen, ch))