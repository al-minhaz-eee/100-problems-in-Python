"""
74.Write a program to print the shape of a matrix.
"""
def shape_(matrix):
    length =[]
    for row in matrix:
        length.append(len(row))
    return len(matrix), max(length)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, -1, -2]
]
r , c = shape_(matrix)
print(f"Shape of matrix {r} by {c}")
