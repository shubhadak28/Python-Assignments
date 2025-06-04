class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def show_vehicle_info(self):
        return f"Vehicle Brand: {self.brand}, Wheels: {self.wheels}"

class Car(Vehicle):
    def __init__(self, brand, wheels, fuel_type, seats):
        super().__init__(brand, wheels)  # Call Vehicle constructor
        self.fuel_type = fuel_type
        self.seats = seats

    def show_car_info(self):
        return f"Fuel Type: {self.fuel_type}, Seats: {self.seats}"

class ElectricCar(Car):
    def __init__(self, brand, wheels, battery_capacity, range_km):
        super().__init__(brand, wheels, fuel_type="Electric", seats=5)  # Electric cars default
        self.battery_capacity = battery_capacity  # in kWh
        self.range_km = range_km  # in kilometers

    def show_electric_info(self):
        return f"Battery: {self.battery_capacity} kWh, Range: {self.range_km} km"

# Create ElectricCar object
e_car = ElectricCar("Tesla", 4, 75, 400)

print(e_car.show_vehicle_info())   # From Vehicle
print(e_car.show_car_info())       # From Car
print(e_car.show_electric_info())  # From ElectricCar
