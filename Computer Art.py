#--------------------------------------------------------------------------------------------------
#
#   Hugo Hartono                                                                                   
#   Modern Computer Art (MCA)
#   15th of February, 2019
#
#--------------------------------------------------------------------------------------------------
from turtle import *
from random import *

def colourRand():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)

def coordRand():
    penup()
    xCoor = randint(-300, 300)
    yCoor = randint(-300, 300)
    goto(xCoor, yCoor)
    pendown()
    
def directRand():
    degree = randint(1, 360)
    setheading(degree)

colormode(255)

shape('turtle')

for t in range(20):
    colourRand()
    coordRand()
    directRand()
    stamp()

def drawRect():     # This function draws a rectangle.
    colourRand()
    coordRand()
    hideturtle()
    length = randint(10, 200)
    width = randint(10, 200)
    begin_fill()
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    end_fill()
    
setheading(0)

for r in range(20):
    drawRect()

def drawCirc():
     colourRand()
     coordRand()
     dot(randint(10, 200))

for c in range(20):
    drawCirc()

    



