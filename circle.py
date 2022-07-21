import math
from distance import distance
from area_circle import area

def circle(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


print(circle(1, 2, 3, 4))