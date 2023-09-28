"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02 import base
from homework_02 import exceptions


class Plane(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, add_weight):
        if self.cargo + add_weight < self.max_cargo:
            self.cargo += add_weight
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        throw_cargo = self.cargo
        self.cargo = 0
        return throw_cargo