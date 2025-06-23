class Circle():
    def __init__(self, radius):
        self.radius = radius


    def get_area(self):
        self.area = 3.14 * pow(self.radius,2)
        return self.area


circle_1 = Circle(2)
print(circle_1.get_area())

circle_2 = Circle(10)
print(circle_2.get_area())

circle_3 = Circle(20)
print(circle_3.get_area())