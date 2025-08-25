import turtle
pen = turtle.Turtle()
pen.speed(3)



def ring(dia, color):
  pen.fillcolor(color)
  pen.begin_fill()
  pen.circle(dia)
  pen.end_fill()
  
  
# Ears
pen.up()
pen.setpos(-45, 85)
pen.down()
ring(15, "black")

pen.up()
pen.setpos(45, 85)
pen.down()
ring(15, "black")

# Face
pen.up()
pen.setpos(0, -10)
pen.down()
ring(60, "white")

# Eyes
pen.up()
pen.setpos(-25, 50)
pen.down()
ring(10, "black")

pen.up()
pen.setpos(25, 50)
pen.down()
ring(10, "black")

pen.up()
pen.setpos(-25, 50)
pen.down()
ring(5, "white")

pen.up()
pen.setpos(25, 50)
pen.down()
ring(5, "white")

# Nose
pen.up()
pen.setpos(0, 20)
pen.down()
ring(4, "black")

# Mouth
pen.up()
pen.setpos(0, 20)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(0, 20)
pen.down()
pen.left(360)
pen.circle(5, -180)

pen.hideturtle()


turtle.done()