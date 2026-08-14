import unittest
import math
from sci_calc import (
    addition, subtraction, multiplication, division, power,
    square_root, modulus, logarithm, factorial, floor_division,
    sine, cosine, tangent, exponential, sec, cosec, cot
)

class TestScientificCalculator(unittest.TestCase):

    def test_basic_arithmetic(self):
        self.assertEqual(addition(5, 6), 11.0)
        self.assertEqual(subtraction(10, 4), 6.0)
        self.assertEqual(multiplication(3, 7), 21.0)
        self.assertEqual(division(20, 5), 4.0)
        self.assertEqual(power(2, 3), 8.0)
        self.assertEqual(modulus(10, 3), 1.0)
        self.assertEqual(floor_division(10, 3), 3.0)

    def test_division_by_zero(self):
        self.assertEqual(division(10, 0), "Error: Division by zero.")
        self.assertEqual(modulus(10, 0), "Error: Division by zero.")
        self.assertEqual(floor_division(10, 0), "Error: Division by zero.")

    def test_square_root(self):
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(-4), "Error: Negative value.")

    def test_logarithm(self):
        self.assertEqual(logarithm(100, 10), 2.0)
        self.assertEqual(logarithm(8, 2), 3.0)
        # Fractional base test
        self.assertEqual(logarithm(0.25, 0.5), 2.0)
        self.assertEqual(logarithm(-10, 10), "Error: Invalid input.")
        self.assertEqual(logarithm(10, 1), "Error: Invalid input.")
        self.assertEqual(logarithm(10, 0), "Error: Invalid input.")
        self.assertEqual(logarithm(10, -2), "Error: Invalid input.")

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-3), "Error: Negative value.")

    def test_trigonometric_functions(self):
        self.assertEqual(sine(0), 0.0)
        self.assertEqual(sine(90), 1.0)
        self.assertEqual(cosine(0), 1.0)
        self.assertEqual(cosine(90), 0.0)
        self.assertEqual(tangent(0), 0.0)
        self.assertEqual(tangent(90), "Error: Undefined.")

    def test_reciprocal_trig_functions(self):
        self.assertEqual(sec(0), 1.0)
        self.assertEqual(sec(90), "Error: Undefined.")
        self.assertEqual(cosec(90), 1.0)
        self.assertEqual(cosec(0), "Error: Undefined.")
        self.assertEqual(cot(45), 1.0)
        self.assertEqual(cot(0), "Error: Undefined.")

    def test_exponential(self):
        self.assertEqual(exponential(0), 1.0)
        self.assertEqual(exponential(1), round(math.e, 6))
        self.assertEqual(exponential(1000), "Error: Overflow.")

if __name__ == "__main__":
    unittest.main()
