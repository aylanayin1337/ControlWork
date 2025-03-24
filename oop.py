"""Задание 1"""
class Person:
    def __init__(self, age=None):
        self._age = None

    def set_age(self, age):
        if age < 0:
            return print("Возраст не может быть отрицательным")
        else:
            self._age = age

    def get_age(self):
        return self._age

p = Person()
p.set_age(25)
print(p.get_age())
p.set_age(-5)


"""Задание 2"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog("Buddy")
cat = Cat("Kitty")

print("------------------")
print(dog.name, dog.speak())
print(cat.name, cat.speak())


"""Задание 3"""
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

print("------------------")
print(move(car))
print(move(bike))

"""Задание 4"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return  round(math.pi * self.radius ** 2, 2)

rect = Rectangle(10, 5)
circle = Circle(7)

print("------------------")
print(rect.area())
print(circle.area())
