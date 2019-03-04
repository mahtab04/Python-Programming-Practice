# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

__author__ = "Mahtab Alam"

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


newRectangle = Rectangle(10, 12)

print(newRectangle.area())
