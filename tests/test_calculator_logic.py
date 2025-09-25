# tests/test_calculator_logic.py
import unittest
from calculator import CalculatorLogic   # <--- cleaner import

class TestCalculatorLogic(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatorLogic()

    def test_append(self):
        self.assertEqual(self.calc.append("12", "3"), "123")

    def test_evaluate_expression(self):
        self.assertEqual(self.calc.evaluate_expression("2+3*4"), "14")
        self.assertEqual(self.calc.evaluate_expression("10/2"), "5.0")

    def test_invalid_expression(self):
        self.assertEqual(self.calc.evaluate_expression("abc"), "Error")

    def test_clear(self):
        self.assertEqual(self.calc.clear(), "")

    def test_backspace(self):
        self.assertEqual(self.calc.backspace("123"), "12")
        self.assertEqual(self.calc.backspace(""), "")

if __name__ == "__main__":
    unittest.main()
