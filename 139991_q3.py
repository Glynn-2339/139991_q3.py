"""Class vehicle sereves as a basis for the other classes"""
class Vehicle:
    def __init__(self, registration_number, make, model):
        """set attributes for generated instances"""
        self.registration_number = registration_number 
        self.make = make
        self.model = model
        
    def display_info(self): #function to display string with vehicle's info
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"

""""""""""""""""""
"""car inherits from vehicle"""
class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model) #Calls for the constructor of the base class (Vehicle) to initialize the common attributes
        self.number_of_seats = number_of_seats

    def display_info(self):
        base_info = super().display_info() #Calls the display_info method to get the basic vehicle information.
        return f"{base_info}, Number of Seats: {self.number_of_seats}"



class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Cargo Capacity: {self.cargo_capacity} kg"



class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Engine Capacity: {self.engine_capacity} cc"

"""this class manages vehicle collection"""
class Fleet:
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        for vehicle in self.vehicles:
            print(vehicle.display_info())

    def search_vehicle_by_registration(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle.display_info()
        return "Vehicle not found."


# this is a dermonstration of functionalities
if __name__ == "__main__":
    fleet = Fleet()

    """adding vehicles to the list"""
    car = Car("ABC123", "Toyota", "Camry", 5)
    truck = Truck("DEF456", "Volvo", "FH16", 20000)
    motorcycle = Motorcycle("GHI789", "Yamaha", "R1", 998)

    fleet.add_vehicle(car)
    fleet.add_vehicle(truck)
    fleet.add_vehicle(motorcycle)

    """Displayingf the vehicles"""
    fleet.display_all_vehicles()

    """ Searching for a vehicle by its registration number"""
    print(fleet.search_vehicle_by_registration("KBS 243X"))
    print(fleet.search_vehicle_by_registration("KCZ 892M"))
"""yeah, i'm tired of this shi"""