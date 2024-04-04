from typing import Union


class Rectangle:
    def __init__(self, base: Union[int, float], heigth: Union[int, float]) -> None:
        self.base = base
        self.heigth = heigth

    def calculate_area(self):
        return self.base * self.heigth

    def calculate_perimeter(self):
        return 2 * (self.base + self.heigth)


calc = Rectangle(5, 10)
print("Área:", calc.calculate_area())
print("Perímetro:", calc.calculate_perimeter())
