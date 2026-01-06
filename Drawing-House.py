import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(3)

# Draw square house base that is brown
t.color("brown")
for in range(4):
    t.forward(100)
    t.left(90)

# Draw roof that is red
t.color("red")
t.left(45)
t.forward(70)
t.left(90)
t.forward(70)

# Move to door position
t.penup()
t.right(135)
t.forward(100)
t.right(90)
t.forward(30)
t.pendown()

# Draw the door that is blue
t.color("blue")
t.left(90)
t.forward(50)
t.right(90)
t.forward(40)
t.right(90)
t.forward(50)

turtle.done()
