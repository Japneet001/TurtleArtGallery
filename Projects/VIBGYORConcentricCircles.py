# VIBGYOR Concentric circles
import turtle

sc = turtle.Screen()

# Screen background color
sc.bgcolor('black')

pen = turtle.Turtle()
pen.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
pen.width(4)

def ring(rad, color, y):
  pen.up()
  pen.sety(y)
  pen.down()
  pen.color(color)
  pen.circle(rad)



colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
for i in range(len(colors)):
  rad = (i + 1) * 20
  ring(rad, colors[i], -rad)



pen.hideturtle()


turtle.done()