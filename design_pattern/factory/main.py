class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started"

class VehicleFactory:
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()

def client_code(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    print(vehicle.start_engine())

client_code(CarFactory())
client_code(TruckFactory())
