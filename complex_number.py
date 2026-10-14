"""
Complex Number Operations

This module provides a ``Complex_number`` class that supports basic arithmetic operations
on complex numbers, including addition, subtraction, scaling, multiplication, and square
root calculation. 

Classes
-------
Complex_number
    A class representing a complex number with real and imaginary parts.

Methods
-------
__init__(a, b)
    Initialize a new complex number with real part 'a' and imaginary part 'b'.

add(other)
    Add another complex number to this instance.

subtract(other)
    Subtract another complex number from this instance.

scale(value)
    Scale this complex number by a given real number.

multiply(other)
    Multiply this complex number by another complex number.

sqrt()
    Compute the square root of this complex number.
"""

import math

class Complex_number:
    def __init__(self, a, b):
        """
        Initialize a new complex number.

        Args:
            a (float): The real part of the complex number.
            b (float): The imaginary part of the complex number.
        """

        self.a = a
        self.b = b

    def add(self, other):
        """
        Add another complex number to this instance.

        Args:
            other (Complex_number): The other complex number to add.

        Returns:
            Complex_number: The result of the addition.
        """

        return Complex_number(self.a + other.a, self.b + other.b)

    def subtract(self, other):
        """
        Subtract another complex number from this instance.

        Args:
            other (Complex_number): The other complex number to subtract.

        Returns:
            Complex_number: The result of the subtraction.
        """

        return Complex_number(self.a - other.a, self.b - other.b)

    def scale(self, value):
        """
        Scale this complex number by a given real number.

        Args:
            value (float): The scaling factor.

        Returns:
            Complex_number: The result of the scaling.
        """

        return Complex_number(self.a * value, self.b * value)

    def multiply(self, other):
        """
        Multiply this complex number by another complex number.

        Args:
            other (Complex_number): The other complex number to multiply with.

        Returns:
            Complex_number: The result of the multiplication.
        """

        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return Complex_number(a, b)

    def sqrt(self):
        """
        Compute the square root of this complex number.

        Returns:
            Complex_number: The square root of this complex number.
        """

        # From complex format to trigonometrical format
        r = math.sqrt(pow(self.a,2) + pow(self.b,2))
        omega = math.atan2(self.b, self.a)

        # Get square root from the trigonometrical form
        r = math.sqrt(r)
        omega = omega / 2

        # Return square root in the original form of the complex number
        return Complex_number(r * math.cos(omega), r * math.sin(omega))

