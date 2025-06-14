class Circle():
    def __init__(self, radius):
        self.radius = radius


    def get_area(self):
        self.area = 3.14 * pow(self.radius,2)
        return self.area


class Person():
    def __init__(self,name):
        self.name = name


class Bus():
    def __init__(self):
        self.max_passengers = 40


    def add_passenger(self,passengers,person):
        if len(passengers) >= self.max_passengers:
            print('The bus is full.')
        else:
            self.max_passengers.append(person)
        return passengers

person_01 = Person('Marco')
passengers = []
bus_01 = Bus()
bus_01.add_passenger(passengers,person_01)