from abc import ABC, abstractmethod

# Every Children of the Vehicle class should HAVE the methods with abstractmethod decorator

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")
        
Car.go()
Car.stop()
        
Motorcycle.go()
Motorcycle.stop()
        
Boat.go()
Boat.stop()