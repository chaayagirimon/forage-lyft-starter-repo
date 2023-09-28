import unittest

class CapuletEngine():
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

class Test(unittest.TestCase):

    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        c = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(c.needs_service())

    def test_needs_service_false(self):
        current_mileage = 300
        last_service_mileage = 0
        c = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(c.needs_service())

if __name__ == "__main__":
    unittest.main()