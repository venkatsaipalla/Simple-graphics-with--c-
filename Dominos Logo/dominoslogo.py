#dominosogo
import turtle
import imp
from turtle import *
t=turtle.Turtle()
t.color("#006393")
t.right(45)
def square():
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
square()

t.penup()
t.goto(5,5)
t.pendown()
t.color("#e8002f")
t.left(90)

square()
t.color("white")
def circle(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

circle(87,-7)
circle(-15,-83)
circle(37,-83)

t.pencolor("#006393")
t.penup()
t.goto(-100,-230)
t.pendown()
t.write("Domino's", font=("Futura",40,"bold"))
t.penup()

t.hideturtle()
done()
wait(10)
turtle.down()