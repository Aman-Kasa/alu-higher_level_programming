def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b are not lists or are not lists of lists,
                   or contain non-numeric elements.
        ValueError: If m_a or m_b are empty, if rows of m_a or m_b have different sizes,
                    or if the matrices cannot be multiplied.
    """
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if multiplication is possible
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            elem_sum = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row_result.append(elem_sum)
        result.append(row_result)

    return result
