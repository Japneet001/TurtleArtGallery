import turtle

def ring(color):
    pen.color(color)
    pen.circle(40)

# Screen
screen = turtle.Screen()
screen.bgcolor("#D1D1D1")

# Pen
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(5)


# Rings
pen.up()
pen.setpos(-100, 15)
pen.down()
ring("blue")

pen.up()
pen.setpos(0, 15)
pen.down()
ring("black")

pen.up()
pen.setpos(100, 15)
pen.down()
ring("red")

pen.up()
pen.setpos(-50, -15)
pen.down()
ring("yellow")

pen.up()
pen.setpos(50, -15)
pen.down()
ring("green")

pen.hideturtle()

turtle.done()