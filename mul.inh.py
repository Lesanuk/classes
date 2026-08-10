
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Rabbit(Prey): # then it gets access to the flee method
    pass

class Hawk(Predator): # then it gets access to the hunt method
    pass

class Fish(Prey, Predator): # then it gets access to both the flee and hunt methods
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# rabbit.flee() # we are invoking the flee method from the Prey class
# hawk.hunt()

# fish.flee()
# fish.hunt() # we can invoke both methods because the Fish class inherits from both Prey and Predator classes

rabbit.eat()
