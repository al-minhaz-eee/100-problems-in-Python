"""
 55.Count the number of vowels in a string provided by the user.
"""
def cout_vowels_in(string):
    count=0
    for vowel in string:
        if vowel in ('AEIOUaeiou') :
           count+=1
    return count
sen = input("Enter your sentece\t ")
print(f"no. of vowels is {cout_vowels_in(sen)}")