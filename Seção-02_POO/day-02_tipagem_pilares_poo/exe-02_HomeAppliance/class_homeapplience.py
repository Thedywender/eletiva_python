from typing import Union


class HomeAppliance:

    AVAILABLE_COLORS = {"VERMELHO", "ROSA", "PRETO", "BRANCO"}

    # Getter
    @property
    def color(self) -> str:
        return self.__color.upper()

    @color.setter  # Repare que é @color.setter, e não @property.setter
    def color(self, new_color: str) -> None:
        if new_color.upper() not in self.AVAILABLE_COLORS:
            raise ValueError(f"A cor '{new_color}' não está disponível")

        self.__color = new_color

    # def get_color(self) -> str:
    #     return self.__color.upper()

    # def set_color(self, new_color: str) -> None:
    #     if new_color.lower() == "turquesa":
    #         raise ValueError("Não existe liquidificador turquesa")

    #     self.__color = new_color

    def __init__(
        self,
        color: str,
        power: int,
        voltage: int,
        price: Union[float, int],
    ) -> None:
        self.price = price
        self.color = color
        self._power = power
        self._voltage = voltage
        self.__max_speed = 3
        self.__speed = 0
        self.turn_off()

    def turn_on(self, speed: int) -> None:
        self.__is_on = True
        self.__speed = speed if speed <= self.__max_speed else self.__max_speed

    def turn_off(self) -> None:
        self.__is_on = False
        self.__speed = 0

    def is_on(self) -> bool:
        return self.__is_on


object1 = HomeAppliance("rosa", 110, 220, 200.1)
print(f"A cor atual é {object1.color}")
object1.color = "preto"
print(f"Mudamos a cor de azul para {object1.color}")
