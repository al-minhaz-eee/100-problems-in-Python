"""
 81. Write a program to swap the key value pair for max and min values
 Eg if the dict is like this {‘a’:1,’b’:2,’c’:3}
 Output should be {a:3,b:2,c:1}
"""
my_dict =  {'a': 1, 'b': 2, 'c': 3}

max_key = max(my_dict, key = my_dict.get)
min_key = min(my_dict, key = my_dict.get)

my_dict[max_key], my_dict[min_key] = my_dict[min_key], my_dict[max_key]

print('updated dictionary', my_dict)