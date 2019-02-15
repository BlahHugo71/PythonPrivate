from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)

for step in range(20):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    
hugo = Turtle()
hugo.color('red')
hugo.shape('turtle')

hugo.penup()
hugo.goto(-160, 100)
hugo.pendown()

lilis = Turtle()
lilis.color('blue')
lilis.shape('turtle')

lilis.penup()
lilis.goto(-160, 70)
lilis.pendown()

dhars = Turtle()
dhars.color('green')
dhars.shape('turtle')

dhars.penup()
dhars.goto(-160, 40)
dhars.pendown()

diana = Turtle()
diana.color('hot pink')
diana.shape('turtle')

diana.penup()
diana.goto(-160, 10)
diana.pendown()

for turn in range(100):
    hugo.forward(randint(1,5))
    lilis.forward(randint(1,5))
    dhars.forward(randint(1,5))
    diana.forward(randint(1,5))

