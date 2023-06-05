import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): First matrix represented as a list of lists.
        m_b (list): Second matrix represented as a list of lists.

    Returns:
        numpy.ndarray: The result of matrix multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied due to incompatible dimensions.

    """
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)

    result = np.matmul(matrix_a, matrix_b)

    return result.tolist()
