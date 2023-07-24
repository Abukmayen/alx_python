#!/usr/bin/env python3


def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C'
        if char not in "cC":
            # If not 'c' or 'C', add it to the result string
            result += char

    return result

if __name__ == "__main__":
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
