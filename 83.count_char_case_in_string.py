"""
 83.Write a function that accepts a string and returns the number of upper
 case chars and lower case chars as a dictionary
"""
def count_case_chars(s):
    case_count = {'uppercase': 0, 'lowercase': 0}
    for char in s:
        if char.isupper():
            case_count['uppercase']+=1
        elif char.islower():
            case_count['lowercase'] +=1
    return case_count

input_string = input("Enter a string: ")

result = count_case_chars(input_string)

print("Character count: ", result)
