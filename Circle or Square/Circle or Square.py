import math
def circle_or_square(rad, area):
    perimeter, circumference = math.sqrt(area) * 4, 2 * math.pi * rad
    return True if circumference > perimeter else False
