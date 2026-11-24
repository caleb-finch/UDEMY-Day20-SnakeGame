import turtle

t = turtle.Turtle()
t.penup()  # Prevents drawing a line when moving
t.goto(0, 50)

# Write text with custom alignment and font
t.write("Hello, Turtle!", move=False, align="center", font=("Times New Roman", 40, "bold"))

turtle.done()