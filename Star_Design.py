import turtle

col = ('yellow','red','green','blue','orange','white')
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range(150):
    t.color(col[i%5])
    t.fd(i*4)
    t.lt(150)
    t.width(2)