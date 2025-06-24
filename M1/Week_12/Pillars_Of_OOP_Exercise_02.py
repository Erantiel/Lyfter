from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, diameter, radius):
        self.diameter = diameter
        self.radius = radius


    def calculate_perimeter(self):
        self.perimeter = 3.14 * self.diameter
        return f'The perimeter of the circle with diameter {self.diameter} is {self.perimeter}\n'


    def calculate_area(self):
        self.area = 3.14 * pow(self.radius,2)
        return f'The area of the circle with radius {self.radius} is {self.area}\n'


class Square(Shape):
    def __init__(self, side):
        self.side = side


    def calculate_perimeter(self):
        self.perimeter = 4 * self.side
        return f'The perimeter of the square with sides equal to {self.side} is {self.perimeter}\n'


    def calculate_area(self):
        self.area = self.side * self.side
        return f'The area of the square with sides equal to {self.side} is {self.area}\n'


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def calculate_perimeter(self):
        if self.length != self.width:
            self.perimeter = 2 * (self.length + self.width)
            return f'The perimeter of the rectangle with length {self.length} and width {self.width} is {self.perimeter}\n'
        else:
            return f'The length and width of a rectangle must be different in order to calculate the perimeter.\n'


    def calculate_area(self):
        if self.length != self.width:
            self.area = self.length * self.width
            return f'The area of the rectangle with length {self.length} and width {self.width} is {self.area}\n'
        else:
            return f'The length and width of a rectangle must be different in order to calculate the area.\n'

circle = Circle(2,4)
square = Square(6)
rectangle = Rectangle(4,8)

print(circle.calculate_perimeter())
print(circle.calculate_area())

print(square.calculate_perimeter())
print(square.calculate_area())

print(rectangle.calculate_perimeter())
print(rectangle.calculate_perimeter())
print(rectangle.calculate_area())