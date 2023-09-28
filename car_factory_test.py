import unittest
from datetime import datetime

# local import
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery 
from car import Car
class CarFactory(unittest.TestCase):

    def test_create_calliope(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-3), current_mileage=30001, last_service_mileage=0):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        if car.needs_service():
            self.assertTrue(car.needs_service())
        else:
            self.assertFalse(car.needs_service())
        # return car
    
    def test_create_glissade(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-3), current_mileage=60001, last_service_mileage=0):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        if car.needs_service():
            self.assertTrue(car.needs_service())
        else:
            self.assertFalse(car.needs_service())
        # return car

    def test_create_palindrome(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-3),warning_light_on=True):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        if car.needs_service():
            self.assertTrue(car.needs_service())
        else:
            self.assertFalse(car.needs_service())
        # return car

    def test_create_rorschach(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-5), current_mileage=60001, last_service_mileage=0):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        if car.needs_service():
            self.assertTrue(car.needs_service())
        else:
            self.assertFalse(car.needs_service())
        # return car

    def test_create_thovex(self, current_date=datetime.today().date(), last_service_date=datetime.today().date().replace(year=datetime.today().date().year-5), current_mileage=30001, last_service_mileage=0):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        if car.needs_service():
            self.assertTrue(car.needs_service())
        else:
            self.assertFalse(car.needs_service())
        # return car

if __name__ == "__main__":
    unittest.main()