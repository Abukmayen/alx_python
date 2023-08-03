#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size
Square = __import__('0-square').Square

# Test case 1
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# Test case 2
mysquare = Square(89)
print(type(mysquare))
print(mysquare.__dict__)

# Test case 3
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)
try:
    print(mysquare.size)
except Exception as e:
    print(e)

# Test case 4
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)
try:
    print(mysquare._size)
except Exception as e:
    print(e)
