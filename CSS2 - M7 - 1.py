#-------------------------------------------------------------------------------
#Name: Richard Mance
#Date: 3/4/22

#Purpose: With the methods of a function, calling for the radius of a circle
#-------------------------------------------------------------------------------

import math

def areaOfCircle(r):
    r2 = pow(r, 2)
    area = r2 * math.pi
    print("The area of the circle:", area)

radius = int(input("What's the radius of the circle?: "))

areaOfCircle(radius)


