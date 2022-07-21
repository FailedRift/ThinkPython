#refactoring

import turtle, math

line = turtle.Turtle()

def polyline(t, n, length, angle):
    """Draws n line segments with a given length 
    and angle (in degrees) between them. 
    t is a turtle"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#polyline(line, 5, 100, 40)

def polygon(t, n, length):
    """Draws a polygon with n sides of particular length.
    t is a turtle."""
    angle = 360.0 / n
    polyline(t, n, length, angle)

#polygon(line, 5, 100)

def arc(t, r, angle):
    """Draws an arc segment sweeping a given angle of a circle with radius r
    t is a turtle"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle =  float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    """draws a circle with radius r
    t is turtle"""
    arc(t, r, 360)

