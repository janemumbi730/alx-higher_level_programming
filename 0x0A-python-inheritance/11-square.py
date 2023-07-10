#!/usr/bin/python3
PrevSquare = __import__('10-square').Square
class Square(PrevSquare):
    def __init__(self, size):
        super().__init__(size)

    def __str__(self):
        return '[Square] {0:d}/{0:d}'.format(self.__size)
