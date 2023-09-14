def square_matrix_simple(matrix=[]):
    # Get the number of rows and columns in the input matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    # Create a new matrix to store the squared values
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Loop through the elements of the input matrix and compute their squares
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
