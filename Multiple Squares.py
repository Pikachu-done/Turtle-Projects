import turtle
mult_square=turtle.Turtle()
def Multiple_Squares(length, colour):
    mult_square.pencolor(colour)
    mult_square.pensize(2)
    mult_square.forward(length)
    mult_square.right(90)
    mult_square.forward(length)
    mult_square.right(90)
    mult_square.forward(length)
    mult_square.right(90)
    mult_square.forward(length)
    mult_square.right(90)
    mult_square.setheading(360)
    mult_square.ht()
for i in range(15,100,15):  # The Calulation is Middle Number is Minus b 1st Number and get divided by Last Number for eg: 120 - 75 = 45 and 45 / 15 = 3
   Multiple_Squares(i,'blue')
   turtle.done