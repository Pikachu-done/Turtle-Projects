import turtle
colors = ["violet","yellow","blue","green","white","red","orange"]
sketch = turtle.Pen()
turtle.bgcolor("black")
sketch.speed(90)
for i in range(350):
   sketch.pencolor(colors[i % 5])
   sketch.width(i/100 + 1)
   sketch.forward(i)
   sketch.left(59)