# "Duck Typing" = "If it looks like a duck and quacks like a duck then it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:
    alive = True
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)