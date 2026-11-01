import unittest
import math
import sci_calc

class TestCalculatorArithmetic(unittest.TestCase):
    """Tests arithmetic operations, powers, roots, and edge cases."""

    def test_nominal_arithmetic(self):
        self.assertEqual(sci_calc.addition(5, 3), 8)
        self.assertEqual(sci_calc.subtraction(10, 4), 6)
        self.assertEqual(sci_calc.multiplication(6, 7), 42)
        self.assertEqual(sci_calc.division(20, 5), 4)
        self.assertEqual(sci_calc.floor_division(10, 3), 3)
        self.assertEqual(sci_calc.modulus(10, 3), 1)

    def test_division_by_zero_and_invalid_divisors(self):
        self.assertEqual(sci_calc.division(5, 0), "Error: Division by zero.")
        self.assertEqual(sci_calc.modulus(5, 0), "Error: Division by zero.")
        self.assertEqual(sci_calc.floor_division(5, 0), "Error: Division by zero.")

    def test_powers_and_overflow(self):
        self.assertEqual(sci_calc.power(2, 3), 8)
        self.assertEqual(sci_calc.power(5, 0), 1)
        self.assertEqual(sci_calc.power(0, 5), 0)
        self.assertEqual(sci_calc.power(4, -1), 0.25)
        # Complex output handling
        self.assertEqual(sci_calc.power(-4, 0.5), "Error: Complex result.")
        # Overflow handling
        self.assertEqual(sci_calc.power(10.0, 1000), "Error: Overflow.")

    def test_roots_and_negative_inputs(self):
        self.assertEqual(sci_calc.square_root(16), 4)
        self.assertEqual(sci_calc.square_root(0), 0)
        self.assertEqual(sci_calc.square_root(2), round(math.sqrt(2), 6))
        # Negative square root domain validation
        self.assertEqual(sci_calc.square_root(-9), "Error: Negative value.")
        self.assertEqual(sci_calc.square_root(-0.0001), "Error: Negative value.")

    def test_logarithms_and_base_restrictions(self):
        self.assertEqual(sci_calc.logarithm(100, 10), 2)
        self.assertEqual(sci_calc.logarithm(8, 2), 3)
        self.assertEqual(sci_calc.logarithm(0.25, 0.5), 2)
        self.assertEqual(sci_calc.natural_log(math.e), 1)
        # Invalid inputs (a <= 0 or base <= 0 or base == 1)
        self.assertEqual(sci_calc.logarithm(-5, 10), "Error: Invalid input.")
        self.assertEqual(sci_calc.logarithm(0, 10), "Error: Invalid input.")
        self.assertEqual(sci_calc.logarithm(10, 1), "Error: Invalid input.")
        self.assertEqual(sci_calc.logarithm(10, 0), "Error: Invalid input.")
        self.assertEqual(sci_calc.logarithm(10, -2), "Error: Invalid input.")
        self.assertEqual(sci_calc.natural_log(0), "Error: Invalid input.")
        self.assertEqual(sci_calc.natural_log(-1), "Error: Invalid input.")

    def test_factorial_and_non_integers(self):
        self.assertEqual(sci_calc.factorial(5), 120)
        self.assertEqual(sci_calc.factorial(0), 1)
        self.assertEqual(sci_calc.factorial(1), 1)
        # Negative numbers and floats
        self.assertEqual(sci_calc.factorial(-3), "Error: Invalid input.")
        self.assertEqual(sci_calc.factorial(4.2), "Error: Invalid input.")


class TestCalculatorTrigonometry(unittest.TestCase):
    """Tests trigonometric quadrant boundaries, negative angles, reciprocal, and inverse functions."""

    def test_trigonometric_quadrant_boundaries(self):
        # 0 degrees
        self.assertEqual(sci_calc.sine(0, mode="deg"), 0)
        self.assertEqual(sci_calc.cosine(0, mode="deg"), 1)
        self.assertEqual(sci_calc.tangent(0, mode="deg"), 0)

        # 90 degrees
        self.assertEqual(sci_calc.sine(90, mode="deg"), 1)
        self.assertEqual(sci_calc.cosine(90, mode="deg"), 0)
        self.assertEqual(sci_calc.tangent(90, mode="deg"), "Error: Undefined.")

        # 180 degrees
        self.assertEqual(sci_calc.sine(180, mode="deg"), 0)
        self.assertEqual(sci_calc.cosine(180, mode="deg"), -1)
        self.assertEqual(sci_calc.tangent(180, mode="deg"), 0)

        # 270 degrees
        self.assertEqual(sci_calc.sine(270, mode="deg"), -1)
        self.assertEqual(sci_calc.cosine(270, mode="deg"), 0)
        self.assertEqual(sci_calc.tangent(270, mode="deg"), "Error: Undefined.")

        # 360 degrees
        self.assertEqual(sci_calc.sine(360, mode="deg"), 0)
        self.assertEqual(sci_calc.cosine(360, mode="deg"), 1)
        self.assertEqual(sci_calc.tangent(360, mode="deg"), 0)

    def test_negative_angles(self):
        self.assertEqual(sci_calc.sine(-90, mode="deg"), -1)
        self.assertEqual(sci_calc.cosine(-90, mode="deg"), 0)
        self.assertEqual(sci_calc.cosine(-180, mode="deg"), -1)

    def test_reciprocal_trig_functions(self):
        self.assertEqual(sci_calc.sec(0, mode="deg"), 1)
        self.assertEqual(sci_calc.sec(90, mode="deg"), "Error: Undefined.")
        self.assertEqual(sci_calc.cosec(90, mode="deg"), 1)
        self.assertEqual(sci_calc.cosec(0, mode="deg"), "Error: Undefined.")
        self.assertEqual(sci_calc.cot(45, mode="deg"), 1)
        self.assertEqual(sci_calc.cot(0, mode="deg"), "Error: Undefined.")
        self.assertEqual(sci_calc.cot(90, mode="deg"), 0)

    def test_radian_mode(self):
        self.assertEqual(sci_calc.sine(math.pi / 2, mode="rad"), 1)
        self.assertEqual(sci_calc.cosine(0, mode="rad"), 1)
        self.assertEqual(sci_calc.tangent(math.pi / 4, mode="rad"), 1)

    def test_inverse_trigonometry(self):
        self.assertEqual(sci_calc.arcsin(0, mode="deg"), 0)
        self.assertEqual(sci_calc.arcsin(1, mode="deg"), 90)
        self.assertEqual(sci_calc.arcsin(-1, mode="deg"), -90)
        self.assertEqual(sci_calc.arccos(1, mode="deg"), 0)
        self.assertEqual(sci_calc.arccos(0, mode="deg"), 90)
        self.assertEqual(sci_calc.arctan(1, mode="deg"), 45)
        # Domain errors outside [-1, 1]
        self.assertEqual(sci_calc.arcsin(2, mode="deg"), "Error: Invalid input.")
        self.assertEqual(sci_calc.arcsin(-1.01, mode="deg"), "Error: Invalid input.")
        self.assertEqual(sci_calc.arccos(1.5, mode="deg"), "Error: Invalid input.")

    def test_exponential(self):
        self.assertEqual(sci_calc.exponential(0), 1)
        self.assertEqual(sci_calc.exponential(1), round(math.e, 6))
        self.assertEqual(sci_calc.exponential(1000), "Error: Overflow.")

if __name__ == "__main__":
    unittest.main()
