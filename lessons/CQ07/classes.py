"""Practing classes."""

from lessons.CQ07.point import Point

__author__: str = '730701948'

class Point:

    def __init__(self: float, x=0.0, y=0.0):
        """Establishing x and y."""
        self.x = x
        self.y = y

    def __str__(self):
        """(x,y.)"""
        return self

    def __mul__(self: float, factor: int):
        """Multiplying x and y by the same factor."""
        if isinstance(factor, (int, float)):
        # Isinstance checks that object is in class.
            return Point(self.x * factor, self.y * factor)
        else:
            raise TypeError("Not supported for multiplication.")

    def __add__(self: float, factor: int):
        """Adding the same factor to x and y."""
        if isinstance(factor, (int, float)):
            return Point(self.x + factor, self.y + factor)
        else:
            raise TypeError("Not supported for addition.")