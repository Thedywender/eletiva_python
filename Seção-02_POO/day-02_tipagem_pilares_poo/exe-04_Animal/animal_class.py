class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print(f"{self.name} fazendo som")
