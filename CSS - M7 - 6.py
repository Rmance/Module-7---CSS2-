#-------------------------------------------------------------------------------
#Name: Richard Mance
#Date: 3/4/22

#Purpose: With the methods of a function, creating a bunch of circles in a given radius/size
#Also, adding color to the circles rather than the dull black - using a list
#-------------------------------------------------------------------------------

import turtle


def DrawUnique(size, colors):
    wn = turtle.Screen()
    Cicle = turtle.Turtle()
    Cicle.speed(15)

    for x in range(10):
        c = colors[x % 3]
        Cicle.color(c)
        Cicle.circle(size)
        Cicle.right(int(360/10))

    wn.exitonclick()



mylist = []
print("Enter 3 colors: ")
for i in range (0, 3):
    ele = [str(input())]
    mylist.append(ele)

sz = float(input("Enter size of shape: "))

DrawUnique(sz, mylist)


