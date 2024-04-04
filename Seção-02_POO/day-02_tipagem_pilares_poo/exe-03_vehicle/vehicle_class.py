class Vehicle:
    def __init__(
        self,
        name: str,
        capacity: int,
    ) -> None:
        self.name = name
        self.capacity = capacity

    def move(self, distance: int):
        return (
            f"{self.name} carried {self.capacity} people across {distance} kilometers."
        )
