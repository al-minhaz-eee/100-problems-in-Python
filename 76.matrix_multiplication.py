"""
76.Write a program to perform matrix multiplication on 2 matrices
"""
def maltiplication_of_(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    columns_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    columns_matrix2 = len(matrix2[0])

    if columns_matrix1 != rows_matrix2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    result =[[0 for _ in range()]]
    for i in range(rows_matrix1):
        for j in range(columns_matrix2):
            for k in range(columns_matrix1):
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]
print(maltiplication_of_(matrix1, matrix2))