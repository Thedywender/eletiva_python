from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self) -> str:
        pass


class Developer(Employee):

    def calculate_bonus(self) -> str:
        return (
            f"O salario do programador {self.name} mais a "
            f"bonificação é de R${'{:.2f}'.format(self.salary *1.2)}"
        )


class Analyst(Employee):
    def calculate_bonus(self) -> str:
        return (
            f"O salario do analista {self.name} mais a "
            f"bonificação é de R${'{:.2f}'.format(self.salary *1.3)}"
        )


class Manager(Employee):
    def calculate_bonus(self) -> str:
        return (
            f"O salario do gerente {self.name} mais a "
            f"bonificação é de R${'{:.2f}'.format(self.salary *1.4)}"
        )


class Worker(Employee):
    def calculate_bonus(self) -> str:
        return (
            f"O salario do gerente {self.name} mais a "
            f"bonificação é de R${'{:.2f}'.format(self.salary *1.4)}"
        )


def main():
    developer = Developer("Rafa", 1500)
    print(developer.calculate_bonus())

    analista = Analyst("Bruno", 1600)
    print(analista.calculate_bonus())

    gerente = Manager("Leandro", 1800)
    print(gerente.calculate_bonus())

    trabalhador = Worker("Fabio", 1200)
    print(trabalhador.calculate_bonus())


if __name__ == "__main__":
    main()
