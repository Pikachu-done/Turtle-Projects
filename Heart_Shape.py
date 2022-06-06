# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()
# turtle.speed(10)

# Defining a method to draw curve
def curve():
	for i in range(208):
		# Defining step by step curve motion
		pen.right(1)
		pen.forward(1)

# # Defining method to draw a full heart
def heart():

	# Set the fill color to red
	pen.fillcolor('red')

	# Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(130)

	# Draw the left curve
	curve()
	pen.left(140)

	# # Draw the right curve
	curve()

	# # Draw the right line
	pen.forward(130)

	# # Ending the filling of the color
	pen.end_fill()

# # Defining method to write text
# def txt():

# 	# Move turtle to air
# 	pen.up()

# 	# Move turtle to a given position
# 	pen.setpos(-43, 85)

# 	# Move the turtle to the ground
# 	pen.down()

# 	# Set the text color to lightgreen
# 	pen.color('lightgreen')

# 	# Write the specified text in
# 	# specified font style and size
# 	pen.write("Tanish", font=("calibri", 27, "bold"))


# Draw a heart
heart()

# Write text
# txt()

# To hide turtle
pen.ht()

turtle.done()
