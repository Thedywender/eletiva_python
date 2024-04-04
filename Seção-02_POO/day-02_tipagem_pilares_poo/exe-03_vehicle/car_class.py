from vehicle_class import Vehicle


class Car(Vehicle):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.name = name
        self.capacity = capacity

    def move(self, distance: int):
        return f"Car {self.name} carried {self.capacity} people across {distance} kilometers."


my_car = Car("S10", 5)
print(my_car.move(20))
