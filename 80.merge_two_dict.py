"""
 80.Write a program to merge two given dictionary
"""

dictionary1 = {
    1:"apple",
    2:"banana"
}
dictionary2 = {
    3:"orange",
    4:"Suger"
}
dictionary1.update(dictionary2)
print(f"Merge dictionery is {dictionary1}")