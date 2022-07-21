import math

def distance(x1, y1, x2, y2):
    '''Calculates the distance between 2 points with coordinates:
    (x1, y1) and (x2, y2) using pythagoras theorem'''
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result


distance(1, 2, 4, 6)
