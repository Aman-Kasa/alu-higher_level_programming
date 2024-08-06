#!/usr/bin/python3
"""
Module for matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.
    
    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.
    
    Returns:
        list of lists of int/float: The result of the multiplication.
    
    Raises:
        TypeError: If m_a or m_b is not a list of lists, or if their elements
        are not integers or floats.
        ValueError: If m_a or m_b is empty, or if they cannot be multiplied.
    """
    
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not all(row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not all(row for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
