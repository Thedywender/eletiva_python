from mammal import Mammal


class Dog(Mammal):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = name

    def bark(self):
        print(f"{self.name} faz Au au!")


dog = Dog("keruba")
dog.make_sound()
dog.bark()
dog.breastfeed()
