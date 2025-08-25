# Tic Tac Toe Board

import turtle
pen = turtle.Turtle()
pen.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
pen.pensize(5)

# Horizontal Lines
pen.up()
pen.setpos(-90, -30)
pen.down()
pen.fd(180)

pen.up()
pen.setpos(-90, 30)
pen.down()
pen.fd(180)

# Vertical Lines
pen.left(90)

pen.up()
pen.setpos(-30, -90)
pen.down()
pen.fd(180)

pen.up()
pen.setpos(30, -90)
pen.down()
pen.fd(180)

pen.hideturtle()


turtle.done()