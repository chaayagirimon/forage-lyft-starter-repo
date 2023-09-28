import unittest

class WilloughbyEngine():
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000

class Test(unittest.TestCase):

    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        w = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(w.needs_service())

    def test_needs_service_false(self):
        current_mileage = 600
        last_service_mileage = 0
        w = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(w.needs_service())

if __name__ == "__main__":
    unittest.main()