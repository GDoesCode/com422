from Car import Car
from pprint import pprint

car1 = Car("Car 1", 220, 200, 5, "Red", True, 1.2, 0)
car2 = Car("Car 2", 30, 180, 7, "Black", False, 2.2, 100)

pprint(vars(car1))
print()
pprint(vars(car2))

car1.accelerate(10)
car2.brake(5)
print(f"{car1.car_name}:\n"
      f"fuel = {car1.fuel_level}\n"
      f"current speed = {car1.current_speed}\n"
      f"{car2.car_name}:\n"
      f"current speed = {car2.current_speed}\n")
car1.refuel(120)
print(f"{car1.car_name}:\n"
      f"fuel = {car1.fuel_level}\n"
      f"current speed = {car1.current_speed}\n"
      f"{car2.car_name}:\n"
      f"current speed = {car2.current_speed}\n")
