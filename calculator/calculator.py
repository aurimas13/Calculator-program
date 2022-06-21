# The calculator & main file
# Calculator program | calculator.py
#
# Created by Aurimas A. Nausedas on 05/15/21.
# Uploaded by Aurimas A. Nausedas on 05/29/21.
# Updated by Aurimas A. Nausedas on 11/23/21.

import math
from typing import Any, Union
""" Importing typing module cause in methods I have two different return values, hence to solve some mypy errors
	I am using Union and Any for returning floats or None and if it breaks str"""

class Calculator:

	""" A Calculator class does mathematical operations like addition,
	subtraction, multiplication, division and taking nth root of a number.
	"""
	
	def __init__(self, memory: float = 0) -> None:
		"""Initializes default value to 0 if not set)
		"""
		self.__memory = memory

	def get_memory(self) -> Union[float, str]:
		"""Gets the memory value 
		>>> calculator = Calculator(4.0)
		>>> calculator.get_memory()
		4.0
		"""
		try: 
			return self.__memory
		except ValueError:
			return "There shouldn't be a value. Just get_memory()"
		except TypeError:
			return "There shouldn't be a value. Just get_memory()"

	def set_memory(self, new_memory: float) -> Any:
		"""Sets the memory value 
		>>> calculator = Calculator()
		>>> calculator.set_memory(4.0)
		"""
		try: 
			new_memory == float(new_memory)
			self.__memory = new_memory
		except ValueError:
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"

	def add(self, number: float) -> Union[float, str]:
		"""Method to add a float (number) to a default value, which is 0 
		if not set when initialized or whatever when initialized.
		Addition: self.memory + number = c
		>>> calculator = Calculator()
		>>> calculator.add(12.0)
		12.0
		"""
		try:
			"Rounding to four decimals and assignment"
			# addition = self.__memory + number
			# addition = roound(addition, 4)
			self.__memory += number
			return self.__memory
		except ValueError: 
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"
		
	def divide(self, number: float) -> Union[float, str]:
		"""Method to divide default value by a float (number) where default value is 0 if not set
		Division: self.memory / number = c
		>>> calculator = Calculator(8)
		>>> calculator.divide(2)
		4.0
		"""
		try:
			"Rounding to four decimals and assignment"
			# division = self.__memory / number
			# division = round(division, 4)
			self.__memory /= number
			return self.__memory
		except ValueError: 
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"
		except ZeroDivisionError:
			print("You cannot divide by zero. Choose another number!\nError: \n")
			raise 
		
	def multiply(self, number: float) -> Union[float, str]:
		"""Method to multiply a float (number) with a self.memory value, 
		which is 0 if not set.
		Multiplication: self.memory * number = c
		>>> calculator = Calculator(4.0)
		>>> calculator.multiply(4)
		16.0
		"""
		try:
			"Rounding to four decimals and assignment"
			# multiplication = self.__memory * number
			# multiplication = round(multiplication, 4)
			self.__memory *= number
			return self.__memory
		except ValueError: 
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"
		
	def subtract(self, number: float) -> Union[float, str]:
		"""Method to subtract a float (number) from a default value, which is 0 if not set
		Subtraction: self.memory - number = c
		>>> calculator = Calculator(4)
		>>> calculator.subtract(2.0)
		2.0
		"""
		try:
			"Rounding to four decimals and assignment"
			# subtraction = self.__memory - number
			# subtraction = round(subtraction, 4)
			self.__memory -= number
			return self.__memory
		except ValueError: 
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"

	def root(self, root_of_number: float) -> Union[float, str]:
		"""Method to take the root (n) of a float. 
		This method prints only real roots.
		Imaginary roots are not printed.
		>>> calculator = Calculator(16)
		>>> calculator.root(2.0)
		4.0
		"""
		try:
			if root_of_number == 0:
				raise ValueError("Oth root is undefined. Please choose a root (n) to be n < 0 or n > 0")
			else:
				pass
			if self.__memory > 0:
				number_after_root = self.__memory**(1.0/root_of_number)
				self.__memory = number_after_root
			elif self.__memory < 0:
				"Because roots of a negative numbers give real and imaginary parts, this part " \
				"gives only real root of a negative number"
				number_after_root = -abs(self.__memory)**(1.0/root_of_number)
				self.__memory = number_after_root
			else:
				if root_of_number > 0:
					self.__memory = 0
				else:
					self.__memory = math.inf
			return self.__memory
		except ValueError as err: 
			return 'The error is: {}'.format(err)
		except ZeroDivisionError: 
			return "Take a value that is non zero"
		except TypeError:
			return "The value should be a float"
		
	def allocate(self, number: float) -> Union[float, str]:
		"""Select the mmory value by passing argument number (example number = 8)
		>>> calculator = Calculator()
		>>> calculator.allocate(8)
		8
		"""	
		try:
			"Assignments"
			self.__memory = number
			return self.__memory
		except ValueError:
			return "The value should be a float"
		except TypeError:
			return "The value should be a float"

	def reset(self) -> Any:
		"""Method to reset memory value
		>>> calculator = Calculator()
		>>> calculator.reset()
		0
		>>> calculator.allocate(16)
		16
		"""
		try:
			self.__memory = 0
			print(self.__memory)
		except ValueError:
			return "There shouldn't be a value. Just reset()"
		except TypeError:
			return "There shouldn't be a value. Just reset()"
