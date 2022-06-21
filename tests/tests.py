# Tests file
# Calculator program | tests.py
#
# Created by Aurimas A. Nausedas on 05/15/21.
# Uploaded by Aurimas A. Nausedas on 05/31/21.
# Updated by Aurimas A. Nausedas on 11/05/21.

# Updated by Aurimas A. Nausedas on 11/05/21.

import pytest
import math
from calculator.calculator import Calculator


def test_addition_when_memory_value_equal_to_zero():
	"""test of add method to see how it handles when you pass 2, 3.3222, 44 and class is initialized to zero"""
	_calculator = Calculator()
	additives = [2, 3.3222, 44]
	products = [2, 5.3222000000000005, 49.3222]
	for index, additive in enumerate(additives):
		assert _calculator.add(additive) == products[index]


def test_addition_when_memory_value_equal_to_one_various_range():
	"""test of add method to see how it handles when you pass 0, 10, -13 and class is initialized to one"""
	_calculator = Calculator(1)
	additives = [0, 10, -13]
	products = [1, 11, -2]
	for index, additive in enumerate(additives):
		assert _calculator.add(additive) == products[index]


def test_addition_when_memory_value_equal_to_negative_one_various_range():
	"""test of add method to see how it handles when you pass -77, 0, 184.55 and class is initialized to -73"""
	_calculator = Calculator(-73)
	additives = [0, -77, 184.55]
	products = [-73, -150, 34.55000000000001]
	for index, additive in enumerate(additives):
		assert _calculator.add(additive) == products[index]


def test_subtraction_when_memory_value_equal_to_zero():
	"""test of subtract method to see how it handles when you pass range from -1 to 1 and class is initialized to zero"""
	_calculator = Calculator()
	for a in range(-1, 1):
		if a == 1:
			assert _calculator.subtract(a) == 0
		else:
			assert _calculator.subtract(a) == 1


def test_subtraction_when_memory_value_equal_to_negative_one_positive_range():
	"""test of subtract method to see how it handles when you pass -57, 0, 74.55 and class is initialized to negative one"""
	_calculator = Calculator(-1)
	subtractives = [-57, 0, 74.55]
	products = [56, 56, -18.549999999999997]
	for index, subtractive in enumerate(subtractives):
		assert _calculator.subtract(subtractive) == products[index]


def test_subtraction_when_memory_value_equal_to_one_positive_range():
	"""test of subtract method to see how it handles when you pass -17, 0, 41 and class is initialized to one"""
	_calculator = Calculator(1)
	subtractives = [-17, 0, 41]
	products = [18, 18, -23]
	for index, subtractive in enumerate(subtractives):
		assert _calculator.subtract(subtractive) == products[index]
	

def test_multiplication_when_memory_value_equal_to_zero():
	"""test of multiply method to see how it handles when you pass range from -1 to 1 and class is initialized to zero"""
	_calculator = Calculator()
	for a in range(-1, 1):
		assert _calculator.multiply(a) == 0


def test_multiplication_when_memory_value_equal_to_negative_one_positive_range():
	"""test of multiply method to see how it handles when you pass positive numbers and class is initialized to negative one"""
	_calculator = Calculator(-1)
	multipliers = [2, 3.4, 4]
	products = [-2, -6.8, -27.2]
	for index, multiplier in enumerate(multipliers):
		assert _calculator.multiply(multiplier) == products[index]


def test_multiplication_when_memory_value_equal_to_negative_eight_various_inputs():
	"""test of multiply method to see how it handles when you pass 8, -10, 0 and class is initialized to negative one"""
	_calculator = Calculator(-8)
	multipliers = [8.5, -10, 0]
	products = [-68.0, 680, 0]
	for index, multiplier in enumerate(multipliers):
		assert _calculator.multiply(multiplier) == products[index]


def test_multiplication_when_memory_value_equal_to_one_positive_range():
	"""test of multiply method to see how it handles when you pass positive numbers and class is initialized to one"""
	_calculator = Calculator(1)
	multipliers = [2, 3, 4]
	products = [2, 6, 24]
	for index, multiplier in enumerate(multipliers):
		assert _calculator.multiply(multiplier) == products[index]


def test_multiplication_when_memory_value_equal_to_one_negative_range():
	"""test of multiply method to see how it handles when you pass negative numbers and class is initialized to one"""
	_calculator = Calculator(1)
	multipliers = [-2, -3, -4]
	products = [-2, 6, -24]
	for index, multiplier in enumerate(multipliers):
		assert _calculator.multiply(multiplier) == products[index]


def test_division_when_memory_value_equal_to_eight_and_root_is_zero():
	"""test of divide method to see how it handles when you pass root as zero and class is initialized to 8"""
	_calculator = Calculator(8)
	with pytest.raises(ZeroDivisionError):
		assert _calculator.divide(0)			


def test_division_when_memory_value_equal_to_one_positive_range():
	"""test of divide method to see how it handles when you pass -12, 2, 8 and class is initialized to 24"""
	_calculator = Calculator(24)
	divisors = [-12, 2, 8]
	products = [-2, -1, -0.125]
	for index, divisor in enumerate(divisors):
		assert _calculator.divide(divisor) == products[index]


def test_division_when_memory_value_equal_to_one_negative_range():
	"""test of divide method to see how it handles when you pass negative numbers and class is initialized to one"""
	_calculator = Calculator(1)
	divisors = [-2, -3, -4]
	products = [-0.5, 0.16666666666666666, -0.041666666666666664]
	for index, divisor in enumerate(divisors):
		assert _calculator.divide(divisor) == products[index]


def test_division_when_memory_value_equal_to_negative_one_positive_range():
	"""test of divide method to see how it handles when you pass -12, 0.5, -2 and class
	is initialized to negative 24"""
	_calculator = Calculator(-24)

	divisors = [-12, 0.5, -2]
	products = [2, 4, -2]
	for index, divisor in enumerate(divisors):
		assert _calculator.divide(divisor) == products[index]


def test_division_when_memory_value_equal_to_negative_one_negative_range():
	"""test of divide method to see how it handles when you pass 0.125, -2, 4 and class
	is initialized to negative one"""
	_calculator = Calculator(-1)

	divisors = [0.125, -2, 4]
	products = [-8, 4, 1]
	for index, divisor in enumerate(divisors):
		assert _calculator.divide(divisor) == products[index]		


def test_root_when_memory_value_equal_to_zero_when_root_is_negative_one():
	"""test of root method to see how it handles when you pass zero root to negative one. This checks an interesting case"""
	_calculator = Calculator(0)
	assert  math.isinf(float(_calculator.root(-1)))
	

def test_root_when_memory_value_equal_to_eight_root_is_positive():
	"""test of root method to see how it handles when the class is initialized to eight and root is 3"""
	_calculator = Calculator(8)
	assert _calculator.root(3) == 2


def test_root_when_memory_value_equal_to_eight_root_is_negative():
	"""test of root method to see how it handles when the class is initialized to eight and root is -3"""
	_calculator = Calculator(8)
	assert _calculator.root(-3) == 0.5


def test_root_when_memory_value_equal_to_one_negative_range():
	"""test of root method to see how it handles when you pass negative numbers and class is initialized to one"""
	_calculator = Calculator(1)
	for a in range(-6, -1):
		assert _calculator.root(a) == 1


def test_root_when_memory_value_equal_to_negative_one_negative_range():
	"""test of root method to see how it handles negative roots when class is initialized to negative one"""
	_calculator = Calculator(-1)
	for a in range(-100, 0):
		assert _calculator.root(a) == -1



