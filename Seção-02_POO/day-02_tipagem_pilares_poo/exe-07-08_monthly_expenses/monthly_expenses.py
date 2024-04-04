class Momthly_expenses:
    def __init__(
        self, internet: float, grocery: float, power: float, water: float, rent: float
    ) -> None:
        self.internet = internet
        self.grocery = grocery
        self._power = power
        self._water = water
        self.__rent = rent

        @property
        def water(self):
            return self._water

        @water.setter
        def water(self, new_value: float):
            if new_value <= 0:
                raise ValueError("O valor deve ser maior que zero")
            self._water = new_value

        @property
        def power(self):
            return self._power

        @power.setter
        def power(self, new_power):
            if new_power <= 0:
                raise ValueError("O valor deve ser maior que zero")
            self._power = new_power
