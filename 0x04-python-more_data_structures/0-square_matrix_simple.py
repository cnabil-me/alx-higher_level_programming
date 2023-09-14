def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    new_matrix = []
    for row in matrix:
        sub_matrix = []
        for item in row:
            sub_matrix.append(item*item)

        new_matrix.append(sub_matrix)
    return new_matrix
