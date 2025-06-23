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
        self.passengers = []


    def add_passenger(self,person):
        if len(self.passengers) >= self.max_passengers:
            print('The bus is full.')
        else:
            self.passengers.append(person)
            return self.passengers


    def remove_passenger(self):
        self.passengers.pop()
        return self.passengers

person_01 = Person('Luis')
person_02 = Person('Marco')
person_03 = Person('Karen')
person_04 = Person('Ana')
bus_01 = Bus()
bus_02 = Bus()
bus_02.max_passengers = 2
print(bus_01.add_passenger(person_01))
bus_01.add_passenger(person_02)
print(bus_02.add_passenger(person_03))
print(bus_02.add_passenger(person_04))
print(bus_02.remove_passenger())