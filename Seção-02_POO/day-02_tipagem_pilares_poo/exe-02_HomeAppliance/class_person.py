from blender import Blender


class Person:
    def __init__(self, name: str, account_balance: float) -> None:
        self.name = name
        self.account_balance = account_balance
        self.blender: Blender | None = None

    def buy_blender(self, blender: Blender) -> str:
        if blender.price <= self.account_balance:
            self.account_balance -= blender.price
            self.blender = blender
            return f"{self.name} comprou um liquidificador por {blender.price} e ficou com R${self.account_balance} na conta!"
        else:
            return (
                f"{self.name} não tem saldo suficiente para comprar o liquidificador."
            )


person = Person("Jacquin", 1000.0)
red_blender = Blender("red", 1000, 220, 350.0)
print(person.buy_blender(red_blender))
