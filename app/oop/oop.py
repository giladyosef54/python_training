from abc import abstractmethod, ABC
from math import pi


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{type(self)}, color: {self.color}'


class Rectangle(Shape):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def __str__(self):
        return str(super()) + f", height: {self.height}, width: {self.width}"

    def __add__(self, rect_to_sum):
        return Rectangle(self.color, self.height + rect_to_sum.height, self.width + rect_to_sum.width)



class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter/2

    def area(self):
        return pi * self._radius**2

    def __str__(self):
        return str(super()) + f', radius: {self._radius}'

    def __add__(self, circle_to_sum):
        return Circle(self.color, self._radius + circle_to_sum._radius)

    def __lt__(self, compared_circle):
        return self._radius < compared_circle

    def __gt__(self, compared_circle):
        return self._radius > compared_circle





