from vehicle_class import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, name, capacity: int = 2) -> None:
        super().__init__(name, capacity)
        self.name = name
        self.capacity = capacity

    def move(self, distance: int):
        return f"Motorcycle {self.name} carried {self.capacity} people across {distance} kilometers."


my_bike = Motorcycle("XBR 1200cc")
print(my_bike.move(10))
