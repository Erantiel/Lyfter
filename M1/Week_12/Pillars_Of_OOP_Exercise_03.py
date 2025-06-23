class Animal:
    def __init__(self,species):
        self.species = species


    def eat(self):
        return print(f'The species of {self.species} can eat.\n')


class Land(Animal):
    def walk(self):
        return print(f'The species of {self.species} can walk over terrain.\n')


class Water(Animal):
    def swim(self):
        return print(f'The species of {self.species} can swim under the water.\n')


class Flyers(Animal):
    def fly(self):
        return print(f'The species of {self.species} can fly over the lands.\n')


class Bear(Land):
    pass


class Bird(Land, Flyers):
    pass


class Amphibian(Land, Water):
    pass

grizzly_bear = Bear('Grizzly Bear')
hawk = Bird('Hawk')
frog = Amphibian('Frog')

grizzly_bear.eat()
grizzly_bear.walk()

hawk.eat()
hawk.walk()
hawk.fly()

frog.eat()
frog.walk()
frog.swim()