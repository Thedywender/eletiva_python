from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def print_price(self):
        NotImplementedError("Precisa implementar o método")


class Book(Product):
    def __init__(self, livro: str, price: float) -> None:
        super().__init__()
        self.price = price
        self.livro = livro

    def print_price(self):
        print(f"O preço do livro {self.livro} é {self.price:.2f}")


livro = Book("A busca do Ponto e virgula", 23.90)
livro.print_price()
