"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'LowFuelError, {0} '.format(self.message)
        else:
            return 'LowFuelError has been raised'


class NotEnoughFuel(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'NotEnoughFuel, {0} '.format(self.message)
        else:
            return 'NotEnoughFuel has been raised'


class CargoOverload(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'CargoOverload, {0} '.format(self.message)
        else:
            return 'CargoOverload has been raised'
