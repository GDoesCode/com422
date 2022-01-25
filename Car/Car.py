class Car:
    def __init__(self, car_name, current_speed, max_speed, no_of_seats, colour, radio, size_of_engine, fuel_level=0):
        self.car_name = str(car_name)
        self.current_speed = int(current_speed)
        self.max_speed = int(max_speed)
        self.no_of_seats = int(no_of_seats)
        self.colour = str(colour)
        self.radio = bool(radio)
        self.size_of_engine = float(size_of_engine)
        self.fuel_level = int(fuel_level)  # Number between 0 and 100

    def accelerate(self, speed_increase):
        if self.fuel_level <= 0:
            self.current_speed = 0
            print("You're out of gas!")
        elif self.current_speed + speed_increase > self.max_speed:
            self.current_speed = self.max_speed
            print("Your dumb, too fast")
            return True
        else:
            self.current_speed += speed_increase
        self.fuel_level -= 1
        return False

    def brake(self, breaking):
        if self.current_speed - breaking < 0:
            self.current_speed = 0
            print("You have stopped!")
        else:
            self.current_speed -= breaking

    def refuel(self, fuel_increase):
        if self.fuel_level + fuel_increase > 100:
            self.fuel_level = 100
            print("Tank is full!")
        else:
            self.fuel_level += fuel_increase
