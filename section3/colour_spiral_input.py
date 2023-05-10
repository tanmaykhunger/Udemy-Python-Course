# ColorSpiralInput.py
import turtle
t = turtle.Pen()
t.speed(-1)
turtle.bgcolor("black")
# Set up a list of any 8 valid Python color names
colors = ["red", "yellow", "blue", "green",
          "orange", "purple", "white", "gray"]
# Ask the user for the number of circles
sides = int( turtle.numinput("Number of circles",
                             "How many circles do you want (1-8)?", 4, 1, 8))
# Draw a colorful spiral with the user-specified number of sides
for x in range(360):
    t.pencolor( colors[x % sides] )
    t.circle(x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)