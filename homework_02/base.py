# import sys
# sys.path.append('C:\\Users\\gremlin\\YandexDisk\\python\\OTUSPythonBasic\\homeworks\\')
from homework_02 import exceptions
from abc import ABC

class Vehicle(ABC):

    def __init__(self, weight=100, fuel=50, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.started = False
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False and self.fuel > 0:
            self.started = True
            print('Vehicle started')
        elif self.started is True:
            print('Vehicle already started')
        else:
            raise exceptions.LowFuelError('Low Fuel')

    def move(self, distance):
        if self.fuel <= 0 and self.fuel_consumption <= 0 and self.fuel <= self.fuel_consumption:
            raise exceptions.NotEnoughFuel('Not Enough Fuel')
        elif self.fuel < (distance * self.fuel_consumption):
            raise exceptions.NotEnoughFuel('Not Enough Fuel')
        else:
            self.fuel -= (distance * self.fuel_consumption)
            print(f'осталось {self.fuel} топлива')
