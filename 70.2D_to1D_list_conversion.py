"""
70.Write a program that can convert a 2D list to 1D listWrite a program that
 can print
"""
def _2Dto1D(lsits):
    return [item for list in lsits for item in list]

two_d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(_2Dto1D(two_d_list))