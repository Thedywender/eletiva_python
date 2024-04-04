from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, cargo) -> None:
        self.cargo = cargo

    @abstractmethod
    def print_role(self):
        pass


class Seller(Person):
    def __init__(self, cargo) -> None:
        super().__init__(cargo)

    def print_role(self):
        print(f"Meu cargo é de {self.cargo}")


class Manager(Person):
    def __init__(self, cargo) -> None:
        super().__init__(cargo)

    def print_role(self):
        print(f"Meu cargo é de {self.cargo}")


seller = Seller("Vendedor")
manager = Manager("Gerente")
seller.print_role()
manager.print_role()
