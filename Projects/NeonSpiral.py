import turtle

screen = turtle.Screen()
screen.bgcolor('black')

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
for i in range(120):    
  t.color('#00FFFF')    
  t.circle(i)    
  t.color('#FF69B4')    
  t.circle(i*0.8)    
  t.right(3)    
  t.forward(3)


turtle.done()