#!/usr/bin/python3
prevRectangle = __import__('8-rectangle').Rectangle


class Rectangle(prevRectangle):
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
