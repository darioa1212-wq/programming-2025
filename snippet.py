import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

mikey = turtle.Turtle()

def draw_spirograph(angle: int):
    mikey.speed(0)
    for _ in range(150):
        mikey.forward(200)
        mikey.left(angle)

def draw_circlespiro(iterations: int):
    mikey.speed(0)
    for _ in range(iterations):
        mikey.circle(100)
        mikey.left(14)

draw_spirograph(89)
mikey.goto(200, 200)
draw_circlespiro(90)


wn.exitonclick()
