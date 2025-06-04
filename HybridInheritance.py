class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_vehicle(self):
        return f"Vehicle Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, car_type):
        super().__init__(brand)
        self.car_type = car_type

    def show_car(self):
        return f"Car Type: {self.car_type}"

class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type

    def show_bike(self):
        return f"Bike Type: {self.bike_type}"

class Electric(Car, Bike):  # Hybrid Inheritance
    def __init__(self, brand, car_type, bike_type, battery_capacity):
        # Call __init__ of both Car and Bike explicitly
        Vehicle.__init__(self, brand)       # Call base class directly once
        self.car_type = car_type
        self.bike_type = bike_type
        self.battery_capacity = battery_capacity

    def show_electric(self):
        return f"Electric Vehicle | Battery: {self.battery_capacity} kWh"

    def show_all(self):
        return (f"{self.show_vehicle()}\n"
                f"Car Type: {self.car_type}\n"
                f"Bike Type: {self.bike_type}\n"
                f"{self.show_electric()}")

# Create Electric object
ev = Electric("Tesla", "Sedan", "Sport Bike", 75)

# Display all details
print(ev.show_all())
