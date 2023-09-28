import unittest

class SternmanEngine():
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on

class Test(unittest.TestCase):

    def test_needs_service_true(self):
        s = SternmanEngine(True)
        self.assertTrue(s.needs_service())

    def test_needs_service_false(self):
        s = SternmanEngine(False)
        self.assertFalse(s.needs_service())

if __name__ == "__main__":
    unittest.main()