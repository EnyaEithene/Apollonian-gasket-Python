"""
Circle Module

This module provides a Circle class to represent circles in a 2D plane, along with
utility functions for validating tangency and drawing circles. The Circle class uses
a Complex_number object to store the center coordinates, and includes methods for drawing
the circle using matplotlib.

Classes
-------
Circle
    A class representing a circle with a center and curvature.

Methods
-------
__init__(x, y, curvature)
    Initialize a new circle with center coordinates (x, y) and curvature.

draw(axes, color, fill)
    Draw the circle on a given matplotlib axes with specified color and fill option.

dist(other)
    Compute the distance between the center of this circle and the center of another circle.

Functions
---------
isTangent(c1, c2, epsilon)
    Check if two circles are tangent to each other within a given tolerance.

validate(c4, triplet, allCircles, epsilon)
    Validate a new circle against a triplet of existing circles and all circles in the scene.
"""

from complex_number import Complex_number
import matplotlib.pyplot as plt
import math

class Circle:
    def __init__(self, x, y, curvature):
        """
        Initialize a new circle.

        Args:
            x (float): The x-coordinate of the circle's center.
            y (float): The y-coordinate of the circle's center.
            curvature (float): The curvature of the circle (1/radius).
        """

        self.center = Complex_number(x, y)
        self.curvature = curvature
        self.radius = abs(1 / self.curvature)

    def draw(self, axes, color="royalblue", fill=True):
        """
        Draw the circle on a given matplotlib axes.

        Args:
            axes (matplotlib.axes.Axes): The axes to draw the circle on.
            color (str, optional): The color of the circle. Defaults to "royalblue".
            fill (bool, optional): Whether to fill the circle. Defaults to True.
        """

        drawing_circle = plt.Circle(
            (self.center.a, self.center.b),
            self.radius,
            facecolor=color if fill else "none",
            edgecolor=color,
            alpha=0.35 if fill else 1.0,
            linewidth=1.2
        )
        axes.add_artist(drawing_circle)

    def dist(self, other):
        """
        Compute the distance between the center of this circle and the center of another circle.

        Args:
            other (Circle): The other circle to compute the distance to.

        Returns:
            float: The distance between the centers of the two circles.
        """

        return math.hypot(
            self.center.a - other.center.a,
            self.center.b - other.center.b
        )

def isTangent(c1, c2, epsilon=1e-6):
    """
    Check if two circles are tangent to each other within a given tolerance.

    Args:
        c1 (Circle): The first circle.
        c2 (Circle): The second circle.
        epsilon (float, optional): The tolerance for checking tangency. Defaults to 1e-6.

    Returns:
        bool: True if the circles are tangent within the given tolerance, False otherwise.
    """

    d = c1.dist(c2)
    r1 = c1.radius
    r2 = c2.radius

    external = abs(d - (r1 + r2)) < epsilon
    internal = abs(d - abs(r1 - r2)) < epsilon

    return external or internal

def validate(c4, triplet, allCircles, epsilon=1e-6):
    """
    Validate a new circle against a triplet of existing circles and all circles in the scene.

    Args:
        c4 (Circle): The new circle to validate.
        triplet (list[Circle]): A triplet of existing circles that the new circle must be tangent to.
        allCircles (list[Circle]): All circles in the scene.
        epsilon (float, optional): The tolerance for validation. Defaults to 1e-6.

    Returns:
        bool: True if the new circle is valid, False otherwise.
    """

    # Stop when circles are too small
    if c4.radius < 2:
        return False

    # Reject duplicate circles
    for other in allCircles:
        same_center = c4.dist(other) < epsilon
        same_radius = abs(c4.radius - other.radius) < epsilon

        if same_center and same_radius:
            return False

    # Require tangency with all three circles
    return all(isTangent(c4, circle, epsilon) for circle in triplet)

