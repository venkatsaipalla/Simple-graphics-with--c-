import imp
from turtle import *

speed(100)
bgcolor('#fb3958')
pencolor('white')
pensize(10)

penup()
goto(100,100)
pendown()

left(180)

def border():
    forward(150)
    for i in range(90):
        forward(1)
        left(1)

border()
border()
border()
border()

penup()
for i in range(90):
    backward(1)
    right(1)
left(90)
pendown()

forward(259)
##
penup()
right(180)
forward(85)
left(120)
pendown()

forward(60)
right(120)

penup()
forward(100)
right(60)
pendown()

forward(60)

penup()
goto(5,-20)
left(60)
right(90)
pendown()

for i in range(3):
    forward(70)
    left(120)
hideturtle()
done()
wait(10)    