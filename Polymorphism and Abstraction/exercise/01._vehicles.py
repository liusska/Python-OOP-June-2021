from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity - distance * self.fuel_consumption >= 0:
            self.fuel_quantity -= distance * self.fuel_consumption + (distance * 0.9)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity - distance * self.fuel_consumption >= 0:
            self.fuel_quantity -= distance * self.fuel_consumption + (distance * 1.6)

    def refuel(self, fuel):
        fuel *= 0.95
        self.fuel_quantity += fuel


