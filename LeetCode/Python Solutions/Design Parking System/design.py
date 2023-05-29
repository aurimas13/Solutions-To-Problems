class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType - 1] > 0:
            self.slots[carType - 1] -= 1
            return True
        return False


# Create a parking system with 3 big, 3 medium, and 3 small slots
parkingSystem = ParkingSystem(3, 3, 3)

# Add cars of different types
car1Added = parkingSystem.addCar(1)  # Big car
car2Added = parkingSystem.addCar(2)  # Medium car
car3Added = parkingSystem.addCar(3)  # Small car

print(f"Car 1 added: {car1Added}")
print(f"Car 2 added: {car2Added}")
print(f"Car 3 added: {car3Added}")
