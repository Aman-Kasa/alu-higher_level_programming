# 0-add_integer.py

def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, defaults to 98.

    Returns:
        int: The sum of a and b, cast to an integer if necessary.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convert both a and b to integers if they are floats
    a = int(a)
    b = int(b)
    
    return a + b
