import unittest
from calculations import session_energy_kwh

class TestCalculations(unittest.TestCase):
    def test_energy_calculation(self):
        appliance = {"wattage": 100, "quantity": 2}
        self.assertAlmostEqual(
            session_energy_kwh(appliance, 3), 0.6
        )

if __name__ == "__main__":
    unittest.main()
