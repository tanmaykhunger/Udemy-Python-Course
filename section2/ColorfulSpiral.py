import turtle
t = turtle.pen()
turtle.speed(1000)
colors = ["red", "yellow", "blue", "green"] 
for x in range(10010):
    turtle.pencolor( colors[ x % 4])
    turtle.forward(x)
    turtle.left(90)
