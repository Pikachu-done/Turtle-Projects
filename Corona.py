import turtle

a = 1
b = 0
turtle.bgcolor('black')
turtle.pencolor('green')
turtle.speed(190)
turtle.penup()
turtle.goto(0,240)
turtle.pendown()
turtle.ht()

while True:
    turtle.fd(a)
    turtle.rt(b)
    a+=3.5
    b+=1
    if b == 210:
        break
turtle.done()                                 
