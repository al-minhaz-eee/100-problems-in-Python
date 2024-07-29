"""
75.Write a program that can check if you can perform matrix
 multiplication on 2 matrices
"""
def shape_(matrix):
    length =[]
    for row in matrix:
        length.append(len(row))
    return len(matrix), max(length)
def is_multipcible(matrix1, matrix2, c1=None):
    r1, c1 = shape_(matrix1)
    r2, c2 = shape_(matrix2)
    return c1==r2

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, -1, -2]
]
matrix2 = [
    [4, 5, 6],
    [7, 8, 9]
]

print(f" {matrix1} and {matrix2} are multicibel {is_multipcible(matrix1, matrix2)}")


