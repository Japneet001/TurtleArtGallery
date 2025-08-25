# Chess Board
import turtle

def square(size_of_square):

  for i in range(4):
    t.forward(size_of_square)
    t.left(90)
  t.forward(size_of_square)


t = turtle.Turtle()
t.speed(5) 

size_of_square = 40

for i in range(8):
  t.up()
  t.setpos(-150, i * size_of_square)
  t.down()

  # rows
  for j in range(8):
    if(i + j) % 2 == 0:
      col = 'black'
    else:
      col = 'white'
    t.fillcolor(col)
    t.begin_fill()
    square(size_of_square)
    t.end_fill()


t.hideturtle()

turtle.done()