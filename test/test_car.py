import unittest
from datetime import datetime

from src.factory import *


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0.3, 0.9, 0.3, 0.3]

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0.3, 0.3, 0.3, 0.3]

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        sensor = [0, 0, 0, 0]

        car = create_palindrome(today, last_service_date, warning_light_is_on, sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        sensor = [0, 0, 0, 0]

        car = create_palindrome(today, last_service_date, warning_light_is_on, sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        sensor = [0, 0, 0, 0]

        car = create_palindrome(today, last_service_date, warning_light_is_on, sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        sensor = [0, 0, 0, 0]

        car = create_palindrome(today, last_service_date, warning_light_is_on, sensor)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_rorschach(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_rorschach(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_rorschach(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_rorschach(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_thovex(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_thovex(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_thovex(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensor = [0, 0, 0, 0]

        car = create_thovex(today, last_service_date, current_mileage, last_service_mileage, sensor)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
