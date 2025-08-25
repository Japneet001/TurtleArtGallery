# Colorful Spiral Web
import turtle
import random

def random_color():
    r = random.randint(0, 255)  # Red value
    g = random.randint(0, 255)  # Green value
    b = random.randint(0, 255)  # Blue value
    return (r, g, b)


screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)    # Set the color mode to allow RGB values

pen = turtle.Turtle()
pen.speed(5)

for x in range(200):
    pen.pencolor(random_color()) # setting color
    pen.width(x/100 + 1) # setting width
    pen.forward(x) # moving forward
    pen.left(59) # moving left

pen.hideturtle()

turtle.done()