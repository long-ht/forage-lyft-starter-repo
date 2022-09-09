from datetime import date

from src.car import Car
from src.engine import *
from src.battery import *
from src.tire import *


def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                    last_service_mileage: int, sensor_data: [float]) -> Car:
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    tire = CarriganTire(sensor_data)
    return Car(engine, battery, tire)


def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                    last_service_mileage: int, sensor_data: [float]) -> Car:
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    tire = CarriganTire(sensor_data)
    return Car(engine, battery, tire)


def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, sensor_data: [float]) -> Car:
    engine = SternmanEngine(warning_light_on)
    battery = SpindlerBattery(last_service_date, current_date)
    tire = CarriganTire(sensor_data)
    return Car(engine, battery, tire)


def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                     last_service_mileage: int, sensor_data: [float]) -> Car:
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    tire = OctoprimeTire(sensor_data)
    return Car(engine, battery, tire)


def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                  last_service_mileage: int, sensor_data: [float]) -> Car:
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    tire = OctoprimeTire(sensor_data)
    return Car(engine, battery, tire)
