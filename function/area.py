# returning multiple value at the sameimport math

import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

Area, Circumferernce = circle_stats(3)

print("Area: ", round(Area,3), "Circumference: ", round(Circumferernce,3))