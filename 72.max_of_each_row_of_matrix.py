"""
write a program that can print the max item of each row of a matrix.
"""
def print_max_of_each_row(matrix):
    for row in matrix:
        max_item = max(row)
        print(f"max item of {row} is {max_item}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, -1, -2]
]
print_max_of_each_row(matrix)