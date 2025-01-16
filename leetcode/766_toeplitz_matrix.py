"""
    766. Toeplitz Matrix
"""


from typing import List

def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    """
        Determines if matrix is toeplitz
    """
    if len(matrix) <= 1 or len(matrix[0]) <= 1:
        return True

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True
