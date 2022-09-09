from datetime import date

from src.car import Car
from src.engine import *
from src.battery import *


def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                    last_service_mileage: int) -> Car:
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)


def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                    last_service_mileage: int) -> Car:
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)


def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
    engine = SternmanEngine(warning_light_on)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)


def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                     last_service_mileage: int) -> Car:
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    return Car(engine, battery)


def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                  last_service_mileage: int) -> Car:
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    return Car(engine, battery)
