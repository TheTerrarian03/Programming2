import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
# leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(3)

# draw flower
painter.color("darkorchid")
painter.goto(20,180)

for petal in range(9):
  painter.right(40)
  painter.forward(60)
  painter.stamp()

painter.penup()
painter.turtlesize(1.75)
painter.color("blue")
painter.goto(-10, 141)
painter.setheading(20)

for petal in range(9):
    painter.right(40)
    painter.forward(30)
    painter.stamp()
  
wn = trtl.Screen()
wn.mainloop()