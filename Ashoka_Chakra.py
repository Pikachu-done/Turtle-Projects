import turtle
from turtle import *

turtle.bgcolor('black')
turtle.speed(500)

for i in range(15):
    for colors in ["blue","red","pink","green","yellow","white","cyan"]:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.lt(11)
        for i in range(4):
            turtle.fd(200)
            turtle.lt(90)       
turtle.done()
