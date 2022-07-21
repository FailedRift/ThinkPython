import math

def hypotenuse(opp, adj):
    hyp = math.sqrt(opp**2 + adj**2)
    return hyp


result = hypotenuse(4, 5)
print(result)