"""
 79.Assume a list with numbers from 1 to 10 and then convert it into a
 dictionary where the key would be the numbers of the list and the
 values would be the square of those numbers
"""
num_list = list(range(1, 11))
square_dict = {
    num : num **2 for num in num_list
}
print(square_dict)