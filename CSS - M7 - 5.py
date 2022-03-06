#-------------------------------------------------------------------------------
#Name: Richard Mance
#Date: 3/4/22

#Purpose: With the methods of a function, creating squares inside of squares - using a loop
#-------------------------------------------------------------------------------

import turtle

def drawSquare(t, sz):
        for x in range(4):
            t.forward(sz)
            t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")


size = float(input("The size of the square: "))
for i in range (10):
    drawSquare(alex, size)
    size = size + 20
    alex.penup()
    alex.goto(alex.pos() + (-10, -10))
    alex.pendown()

wn.exitonclick()