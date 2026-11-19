
f a matrix"""


def determinant(matrix):
    """Calculates the determinant of a non-empty square matrix

    matrix: square list of lists

    Returns: the determinant of matrix
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det


def minor(matrix):
    """Calculates the minor matrix of a non-empty square matrix

    matrix: square list of lists

    Returns: the minor matrix of matrix
    """
    n = len(matrix)
    # The minor of a 1x1 matrix is the determinant of a 0x0 matrix, i.e. 1
    if n == 1:
        return [[1]]

    result = []
    for i in range(n):
        minors_row = []
        for j in range(n):
            sub = [row[:j] + row[j + 1:]
                   for k, row in enumerate(matrix) if k != i]
            minors_row.append(determinant(sub))
        result.append(minors_row)
    return result


def cofactor(matrix):
    """Calculates the cofactor matrix of a non-empty square matrix

    matrix: square list of lists

    Returns: the cofactor matrix of matrix
    """
    n = len(matrix)
    minors = minor(matrix)
    # Cofactor C_ij = (-1)^(i+j) * M_ij
    return [[((-1) ** (i + j)) * minors[i][j] for j in range(n)]
            for i in range(n)]


def adjugate(matrix):
    """Calculates the adjugate matrix of a non-empty square matrix

    matrix: square list of lists

    Returns: the adjugate matrix of matrix
    """
    n = len(matrix)
    cof = cofactor(matrix)
    # The adjugate is the transpose of the cofactor matrix
    return [[cof[j][i] for j in range(n)] for i in range(n)]


def inverse(matrix):
    """Calculates the inverse of a matrix

    matrix: list of lists whose inverse should be calculated

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not square or is empty

    Returns: the inverse of matrix, or None if matrix is singular
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)
    if det == 0:
        return None

    adj = adjugate(matrix)
    # inverse = adjugate / determinant
    return [[adj[i][j] / det for j in range(n)] for i in range(n)]
