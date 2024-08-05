#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle


if __name__ == "__main__":

    # Create a Rectangle instance
    r1 = Rectangle(3, 5, 1)
    
    # Convert instance to dictionary
    r1_dictionary = r1.to_dictionary()
    
    # Create a new Rectangle instance from the dictionary
    r2 = Rectangle.create(**r1_dictionary)
    
    # Print the original and new instances
    print(r1)
    print(r2)
    
    # Check if they are the same instance
    print(r1 is r2)
    
    # Check if they are equal
    print(r1 == r2)
