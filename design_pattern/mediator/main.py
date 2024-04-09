from abc import ABC, abstractmethod

class ATCMediator(ABC):
    """交通管制塔のメディエーターの抽象クラス。"""
    @abstractmethod
    def register_runway(self, runway):
        pass

    @abstractmethod
    def register_flight(self, flight):
        pass

    @abstractmethod
    def can_land(self, flight):
        pass

class Flight:
    """飛行機クラス。"""
    def __init__(self, id, atc_mediator):
        self.id = id
        self.atc_mediator = atc_mediator
        self.atc_mediator.register_flight(self)

    def request_to_land(self):
        if self.atc_mediator.can_land(self):
            return f"Flight {self.id} is landing."
        else:
            return f"Flight {self.id} is waiting for landing."

class Runway:
    """滑走路クラス。"""
    def __init__(self, id, atc_mediator):
        self.id = id
        self.is_available = True
        self.atc_mediator = atc_mediator
        self.atc_mediator.register_runway(self)

class AirportATC(ATCMediator):
    """交通管制塔を実装するクラス。"""
    def __init__(self):
        self.flights = []
        self.runways = []

    def register_runway(self, runway):
        self.runways.append(runway)

    def register_flight(self, flight):
        self.flights.append(flight)

    def can_land(self, flight):
        available_runway = next((runway for runway in self.runways if runway.is_available), None)
        if available_runway:
            available_runway.is_available = False
            return True
        return False

# シミュレーション
atc = AirportATC()
runway1 = Runway("Runway1", atc)

flight1 = Flight("Flight1", atc)
flight2 = Flight("Flight2", atc)

print(flight1.request_to_land())
print(flight2.request_to_land())
