"""
создайте класс `Car`, наследник `Vehicle`
"""
# import sys
# sys.path.append('C:\\Users\\gremlin\\YandexDisk\\python\\OTUSPythonBasic\\homeworks\\')
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        if isinstance(engine, Engine):
            self.engine = engine
