import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_add_calculate(self):
        assert self.calc.adding(self, 3, 4) == 7

    def test_subtract_calculate(self):
        assert self.calc.subtraction(self, 9, 6) == 3

    def test_divide_calculate(self):
        assert self.calc.division(self, 8, 4) == 2
