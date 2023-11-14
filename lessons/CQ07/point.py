"""Practing object oriented programming."""

from __future__ import annotations

__author__: str = '730701948'

class Point:
# attributes 
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """My constructor."""
        self.x = x_init 
        self.y = y_init

    def scale_by(self, factor: int) ->  None:
        """Mutating a point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creating a new point."""
        x = self.x * factor
        y = self.y * factor
        new_point: Point = Point(x, y)
        return new_point

class Point:
    def __init__(self, x=0.0, y=0.0):
        """Establishing x and y."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """(x,y)."""
        product: str = f'x: {self.x}; y: {self.y}'
        return product

    def __mul__(self, factor: int | float) -> Point:
        """Method to overload the multiplication * operator!"""
        product1: float = self.x
        product1 *= factor
        product2: float = self.y
        product2 *= factor
        return Point(product1, product2)

    def __add__(self, factor: int | float) -> Point:
        """Method to overload the addition + operator!"""
        product1: float = self.x
        product1 += factor
        product2: float = self.y
        product2 += factor
        return Point(product1, product2)