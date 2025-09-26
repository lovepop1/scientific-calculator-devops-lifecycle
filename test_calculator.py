# test_calculator.py
import unittest
from calculator import square_root, factorial, natural_log, power

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(9), 3)
        # Test a floating point number
        self.assertAlmostEqual(square_root(2), 1.41421356, places=7)
        # Test for the ValueError with negative numbers
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1) # Edge case
        self.assertEqual(factorial(1), 1) # Edge case
        with self.assertRaises(ValueError):
            factorial(-3)
        with self.assertRaises(ValueError):
            factorial(1.5) # Factorial is for integers only

    def test_natural_log(self):
        # Using assertAlmostEqual for floating point comparisons
        self.assertAlmostEqual(natural_log(1), 0)
        self.assertAlmostEqual(natural_log(2.71828), 1, places=5)
        with self.assertRaises(ValueError):
            natural_log(0)
        with self.assertRaises(ValueError):
            natural_log(-10)
            
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1) # Edge case
        self.assertEqual(power(10, -1), 0.1)
        self.assertAlmostEqual(power(4, 0.5), 2) # Square root equivalent

if __name__ == '__main__':
    unittest.main()