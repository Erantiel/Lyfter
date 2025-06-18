class Person():
    def __init__(self,name):
        self.name = name


    def __str__(self):
        return self.name


    def __repr__(self):
        return self.name


class Bus():
    def __init__(self):
        self.max_passengers = 1


    def add_passenger(self,passengers,person):
        if len(passengers) >= self.max_passengers:
            print('The bus is full.')
        else:
            return person

passengers = []
person_01 = Person('Luis')
person_02 = Person('Marco')
person_03 = Person('Karen')
bus_01 = Bus()
passengers.append(bus_01.add_passenger(passengers,person_01))
passengers.append(bus_01.add_passenger(passengers,person_02))
passengers.append(bus_01.add_passenger(passengers,person_03))

print(passengers)