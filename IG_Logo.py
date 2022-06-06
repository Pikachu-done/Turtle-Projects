from turtle import *

bgcolor('black')
pencolor('white')
width(23)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
    forward(250)
    circle(90,90)

penup()
goto(70,20)
pendown()
circle(119,360)
penup()
goto(115,180)
pendown()
circle(7,360)
ht()
done()