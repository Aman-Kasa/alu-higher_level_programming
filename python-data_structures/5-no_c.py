#!/usr/bin/python3


def no_c(my_string):
    # Initialize an empty list to collect characters that are not 'c' or 'C'
    result = []
    
    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C', then append to result list
        if char != 'c' and char != 'C':
            result.append(char)
    
    # Join the characters in the result list into a new string
    return ''.join(result)


# Test cases as per the provided examples
if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
