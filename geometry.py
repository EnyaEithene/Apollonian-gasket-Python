"""
Geometry Utility Functions for Apollonian Gasket Fractal

This module provides utility functions for computing circles tangent to three given
circles using the Descartes circle theorem. The functions 'descartes' and
'complexDescartes' are used to determine the curvature and centers of new circles
that are tangent to three specified circles.

Functions
--------
descartes
- Computes the two circles tangent to three given circles using the Descartes circle theorem.

complexDescartes
- Computes the two circles tangent to three given circles using the Descartes circle theorem and returns their center coordinates as complex numbers.

Dependencies
------------
- Circle class from 'circle' module (provides curvature, center, radius).
- ComplexNumber class from 'complex_number' module.
"""

from circle import Circle
from complex_number import Complex_number
import math

def descartes(c1, c2, c3):
    """
    Compute the two circles tangent to three given circles using the Descartes circle theorem.

    Args:
        c1 (Circle class object): First input circle.
        c2 (Circle class object): Second input circle.
        c3 (Circle class object): Third input circle.

    Returns:
        list[Circle class object]: A list containing two Circle objects: [c1, c2, new_circle] and [c1, c3, new_circle]. 
                                Each new circle is tangent to the three input circles.
    """

    # The curvature of each given circle
    k1 = c1.curvature 
    k2 = c2.curvature 
    k3 = c3.curvature

    # The components of the Descartes theorem
    sum = k1 + k2 + k3
    root = 2 * math.sqrt(k1 * k2 + k2 * k3 + k1 * k3)

    return [sum + root, sum - root]

def complexDescartes(c1, c2, c3, k4):
    """
    Compute the two circles tangent to three given circles using the Descartes circle theorem.

    Args:
        c1 (Circle class object): First input circle.
        c2 (Circle class object): Second input circle.
        c3 (Circle class object): Third input circle.
        k4 (tuple of two numbers): The curvature of the fourth circle that defines the scaling factor for the returned circles.

    Returns:
        list [Circles class object]: A list containing two ``Circle`` objects: 
                - the first element is tangent to all three input circles,
                - the second element is also tangent to all three input circles. 
            Each Circle object includes its center coordinates (as a Complex_number) and curvature equal to k4[0] and k4[1] respectively.
    """

    # The curvature and center of each given circle
    k1 = c1.curvature 
    k2 = c2.curvature 
    k3 = c3.curvature
    z1 = c1.center
    z2 = c2.center
    z3 = c3.center

    # Components of the complex Descartes theorem
    zk1 = z1.scale(k1)
    zk2 = z2.scale(k2)
    zk3 = z3.scale(k3)
    sum = zk1.add(zk2.add(zk3))
    
    root = zk1.multiply(zk2).add(zk2.multiply(zk3)).add(zk1.multiply(zk3))
    root = root.sqrt().scale(2)
    
    center1 = sum.add(root).scale(1/k4[0])
    center2 = sum.subtract(root).scale(1/k4[0])
    center3 = sum.add(root).scale(1/k4[1])
    center4 = sum.subtract(root).scale(1/k4[1])

    return [Circle(center1.a, center1.b, k4[0]),
            Circle(center2.a, center2.b, k4[0]),
            Circle(center3.a, center3.b, k4[1]),
            Circle(center4.a, center4.b, k4[1])]

