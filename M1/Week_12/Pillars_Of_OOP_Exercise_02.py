from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def calculate_perimeter(self, diameter):
        self.diameter = diameter
        self.perimeter = 3.14 * self.diameter
        return f'The perimeter of the circle with diameter {self.diameter} is {self.perimeter}\n'


    def calculate_area(self, radius):
        self.radius = radius
        self.area = 3.14 * pow(self.radius,2)
        return f'The area of the circle with radius {self.radius} is {self.area}\n'


class Square(Shape):
    def calculate_perimeter(self, side_perimeter):
        self.side_perimeter = side_perimeter
        self.perimeter = 4 * self.side_perimeter
        return f'The perimeter of the square with sides equal to {self.side_perimeter} is {self.perimeter}\n'


    def calculate_area(self, side_area):
        self.side_area = side_area
        self.area = self.side_area * self.side_area
        return f'The area of the square with sides equal to {self.side_area} is {self.area}\n'


class Rectangle(Shape):
    def calculate_perimeter(self, length_perimeter, width_perimeter):
        self.length_perimeter = length_perimeter
        self.width_perimeter = width_perimeter
        if self.length_perimeter != self.width_perimeter:
            self.perimeter = 2 * (self.length_perimeter + self.width_perimeter)
            return f'The perimeter of the rectangle with length {self.length_perimeter} and width {self.width_perimeter} is {self.perimeter}\n'
        else:
            return f'The length and width of a rectangle must be different in order to calculate the perimeter.\n'


    def calculate_area(self, length_area, width_area):
        self.length_area = length_area
        self.width_area = width_area
        if self.length_area != self.width_area:
            self.area = self.length_area * self.width_area
            return f'The area of the rectangle with length {self.length_area} and width {self.width_area} is {self.area}\n'
        else:
            return f'The length and width of a rectangle must be different in order to calculate the area.\n'

circle = Circle()
square = Square()
rectangle = Rectangle()

print(circle.calculate_perimeter(2))
print(circle.calculate_area(2))

print(square.calculate_perimeter(4))
print(square.calculate_area(4))

print(rectangle.calculate_perimeter(2,2))
print(rectangle.calculate_perimeter(2,4))
print(rectangle.calculate_area(2,4))