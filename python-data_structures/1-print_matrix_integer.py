#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            # Print the number with appropriate formatting using str.format()
            print("{:d}".format(num), end="")
            # Add a space after each number except the last one in a row
            if i < len(row) - 1:
                print(" ", end="")
        # Print a new line after each row
        print()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
