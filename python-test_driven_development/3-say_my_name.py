#!/usr/bin/python3
"""A function that prints the name of a user."""

def say_my_name(first_name, last_name=""):
    """
    Function to take in names and print the full name.
    
    Args:
        first_name (str): This is the first argument, and it must be a string.
        last_name (str): This is the second argument, and it must be a string. Defaults to an empty string.
        
    Raises:
        TypeError: If either first_name or last_name is not a string.
        
    Returns:
        None
        
    Prints:
        My name is <first name> <last name>
    
    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob")
        My name is Bob 
        >>> say_my_name(12, "White")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string
        >>> say_my_name("John", 12)
        Traceback (most recent call last):
            ...
        TypeError: last_name must be a string
        >>> say_my_name()
        Traceback (most recent call last):
            ...
        TypeError: missing 1 required positional argument: 'first_name'
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
