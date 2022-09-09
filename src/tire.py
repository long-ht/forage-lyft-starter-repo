from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class CarriganTire(Tire):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def needs_service(self):
        for wear_value in self.sensor_data:
            if wear_value >= 0.9:
                return True
        return False


class OctoprimeTire(Tire):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def needs_service(self):
        if sum(self.sensor_data) >= 3:
            return True
        return False
