from datetime import datetime
import unittest

class SpindlerBattery():
    def __init__(self, last_service_date, current_date):
        # super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date - self.last_service_date).days/365  >= 2.0
    
class Test(unittest.TestCase):

    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year-3)
        s = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(s.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year-1)
        s = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(s.needs_service())

if __name__ == "__main__":
    unittest.main()