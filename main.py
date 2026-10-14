"""
Apollonian Gasket Fractal Visualization

This module creates an interactive visualization of the Apollonian gasket fractal using
matplotlib. When the user clicks on the plot, the ``mousePressed`` function processes
the click, computes a new circle tangent to two existing circles, and adds it to the
drawing queue. The script sets up a fixed enclosing circle, randomly generates
initial circles, and runs an event loop that updates the visualization on each
mouse press.

Functions
--------
main
- Initializes the figure, draws the initial three circles, and starts the
  interactive event loop.

mousePressed
- Processes a mouse‑press event. It receives the current processing queue,
  the list of all circles, and the matplotlib axes. For each stored pair
  of circles (c1, c2, c3) it computes new tangent circles via ``descartes``
  and ``complexDescartes``. Validated circles are added to the queue and
  drawn on the plot. The updated queue is returned for further processing.

Dependencies
------------
- matplotlib: for plotting and interactive canvas
- math: for more advanced mathematical operations
- random: to randomly generate coordinates for the first three circles
- circle: custom module providing a Circle class with a ``draw`` method
- geometry: provides ``descartes`` and ``complexDescartes`` utilities
"""

import matplotlib.pyplot as plt
import math
import random

from circle import Circle, validate, isTangent
from geometry import descartes, complexDescartes

# Global variables
epsilon = 1e-6                      # Error 
width = 800                         # Width and Height of canvas
height = 600
CMAP = plt.colormaps["plasma"]      # Colormap for the circles


def mousePressed(queue, allCircles, axes):
    """
    Handles mouse press events by generating new circles tangent to existing ones.

    Args:
        queue (list): Queue of circle triples [c1, c2, c3] where c1, c2 and c3 are
                    previously defined circles that define tangency points.
        allCircles (list): List of all circles currently in the visual representation. 
                        Used for validation and updating the processing queue.
        axes (matplotlib.axes.Axes): The axes instance associated with the event with which the circles are drawn.

    Returns:
        list: A list of new circle‑triple entries [c1, c2, new_circle] generated from
            the clicked region. Each entry is appended to a new queue for subsequent
            processing.
    """

    nextQueue = []

    for c1, c2, c3 in queue:
        # Find the new circles using the newly found k4 curvature
        k4 = descartes(c1, c2, c3)
        newCircles = complexDescartes(c1, c2, c3, k4)

        # We check that each circle is tangent with the circles we already have
        # Draw them and add them to the queue if true
        for newCircle in newCircles:
            if validate(newCircle, [c1, c2, c3], allCircles, epsilon):
                allCircles.append(newCircle)
                color = CMAP((len(allCircles) % 100) / 99)
                newCircle.draw(axes, color=color)

                nextQueue.append([c1, c2, newCircle])
                nextQueue.append([c1, c3, newCircle])
                nextQueue.append([c2, c3, newCircle])

    axes.figure.canvas.draw_idle()
    return nextQueue 


def main():
    # ===== Randomly generating the first three circles =====
    # c1 - Fixed enclosing circle
    c1 = Circle(width / 2, height / 2, -1 / (width / 2))
    R = c1.radius

    # c2 - First circle inside c1
    r2 = random.uniform(20, R / 2)
    angle = random.uniform(0, 2 * math.pi)

    d2 = R - r2

    x2 = c1.center.a + d2 * math.cos(angle)
    y2 = c1.center.b + d2 * math.sin(angle)

    c2 = Circle(x2, y2, 1 / r2)

    # c3 - Second circle inside c1, tangent to c1 and c2
    # Choose the angle between the directions to c2 and c3.
    theta = random.uniform(math.radians(20), math.radians(160))
    cos_theta = math.cos(theta)

    # Calculate r3 using the tangency conditions.
    r3 = (R * (R - r2) * (1 - cos_theta)
            / (R + r2 - (R - r2) * cos_theta))

    d3 = R - r3

    # Choose which side of c2 to place c3 on.
    direction = random.choice([-1, 1])
    angle3 = angle + direction * theta

    x3 = c1.center.a + d3 * math.cos(angle3)
    y3 = c1.center.b + d3 * math.sin(angle3)

    c3 = Circle(x3, y3, 1 / r3)

    # ===== Finding the circles based on the fractal rules =====
    # Setup for multiple circles
    allCircles = [c1, c2, c3]
    queue = [[c1,c2,c3]]

    # Create one figure for all circles
    figure, axes = plt.subplots()

    # Draw every circle on the same axes (the first three circles)
    for i, circle in enumerate(allCircles):
        color = CMAP(i / max(1, len(allCircles) - 1))
        circle.draw(axes, color=color)

    # ===== Drawing the rest of the circles =====
    # Configure the plot
    axes.set_aspect("equal")
    axes.set_xlim(0, width)
    axes.set_ylim(0, height)
    axes.set_title("Apollonian gasket")

    # Create circles on mouse click
    def on_mouse_press(event):
        nonlocal queue

        if event.inaxes == axes:
            queue = mousePressed(queue, allCircles, axes)

    figure.canvas.mpl_connect(
        "button_press_event",
        on_mouse_press
    )

    # Show plot
    plt.show()

if __name__ == "__main__":
    main()
