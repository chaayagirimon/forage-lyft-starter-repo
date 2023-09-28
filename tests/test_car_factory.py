import unittest
from datetime import datetime

# local import
from test_battery.test_nubbin_battery import NubbinBattery
from test_battery.test_spindler_battery import SpindlerBattery
from test_engine.test_capulet_engine import CapuletEngine
from test_engine.test_sternman_engine import SternmanEngine
from test_engine.test_willoughby_engine import WilloughbyEngine
from car import Car

class CarFactory(unittest.TestCase):

    def test_create_calliope_true(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-3), current_mileage=30001, last_service_mileage=0):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_create_calliope_false(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-1), current_mileage=300, last_service_mileage=0):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())
        
    def test_create_glissade_true(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-3), current_mileage=60001, last_service_mileage=0):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_create_glissade_false(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-1), current_mileage=600, last_service_mileage=0):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

    def test_create_palindrome_true(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-3),warning_light_on=True):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_create_palindrome_false(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-1),warning_light_on=False):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

    def test_create_rorschach_true(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-5), current_mileage=60001, last_service_mileage=0):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_create_rorschach_false(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-3), current_mileage=600, last_service_mileage=0):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

    def test_create_thovex_true(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-5), current_mileage=30001, last_service_mileage=0):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_create_thovex_false(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-3), current_mileage=300, last_service_mileage=0):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

if __name__ == "__main__":
    unittest.main()