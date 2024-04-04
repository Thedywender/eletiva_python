from animal_class import Animal


class Mammal(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = name

    def breastfeed(self):
        print(f"{self.name} amamentando")
