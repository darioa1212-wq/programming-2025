# Recursion
# Author: Ubial
# 20 October

# Create a function that draws trees recursively

import turtle

# Set up the environment
wn = turtle.Screen()
t = turtle.Turtle()
t.left(90)              # point the turtle up
t.penup()               # move the turtle a little lower
t.goto(0, -200)
t.color("brown")
t.width(10)
t.shape("arrow")        # leaf shape
t.shapesize(5)

# Create a dictionary of leaf colours
LEAF_COLOURS = {
    "spring": "#efc3e6",
    "summer": "#4da167",
    "fall": "#7b0d1e",
    "winter": "#cefdff",
}


def draw_tree(level: int, branch_length: float):
    """Draw a tree recursively at a given level
    level - the levels of branches
    branch_length - length of branch in pixels
    """
    t.pendown()

    # If the level is greater than zero
    if level > 0:
        # 1. Move forward branch_length
        t.forward(branch_length)
        # 2. Turn left and draw a "smaller tree"
        t.left(47)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. Turn right and draw a "smaller tree"
        t.right(94)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Return to the beginning
        t.left(47)
        t.backward(branch_length)
    else:  # base case
        # create a leaf
        t.color(LEAF_COLOURS["spring"])
        t.stamp()
        t.color("brown")

def draw_complicated_tree(level: int, branch_length:float):
    """Draws a more complicated tree"""
    t.pendown()
    t.shapesize(2)

    angle = 52

    if level > 0:
        # 1. Move forward branch_length
        t.forward(branch_length)
        # 2. Turn left and draw a "smaller tree"
        t.left(angle)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 3. Turn right and draw a "smaller tree"
        t.right(angle)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        t.right(angle)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 4. Return to the beginning
        t.left(angle)
        t.backward(branch_length)
    else:
        t.color("green")
        t.stamp()
        t.color("brown")

def draw_super_comp_tree(level: int, branch_length:float):
    """Draws a more complicated tree"""
    t.pendown()
    t.shapesize(2)

    angle = 52

    if level > 0:
        # 1. Move forward branch_length
        t.forward(branch_length)
        # 2. Turn left and draw a "smaller tree"
        t.left(angle)
        draw_super_comp_tree(level - 1, branch_length * 0.8)
        # 3. Turn right and draw a "smaller tree"
        t.right(angle / 2)
        draw_super_comp_tree(level - 1, branch_length * 0.8)
        t.right(angle / 2)
        draw_super_comp_tree(level - 1, branch_length * 0.8)
        t.right(angle / 2)
        draw_super_comp_tree(level - 1, branch_length * 0.8)
        t.right(angle / 2)
        draw_super_comp_tree(level - 1, branch_length * 0.8)
        # 4. Return to the beginning
        t.left(angle)
        t.backward(branch_length)
    else:
        t.color("green")
        t.stamp()
        t.color("brown")

def draw_asymmetric_tree(level: int, branch_length: float):
    t.pendown()
    t.shapesize(2)

    if level > 0:
        t.forward(branch_length)

        t.left(73)
        draw_asymmetric_tree(level-1, branch_length * 0.8)
        t.right(73 / 3)
        draw_complicated_tree(level-1, branch_length * 0.8)
        t.right(73 / 3)
        draw_super_comp_tree(level-1, branch_length * 0.8)
        t.right(73 / 3)
        draw_asymmetric_tree(level-1, branch_length * 0.8)

        t.backward(branch_length)

def factorial(num: int) -> int:
    """Calculate the factorial of the
    given num recursively"""
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1

def fibonacci(num: int) -> int:
    """Returns the nth fibonacci number
    calculated recursively"""
    if num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)
    else:
        return 1

# t.speed(0)
# draw_asymmetric_tree(4, 225)

# print(fibonacci(6))            # 8
# print(fibonacci(8))            # 21
# print(fibonacci(20))

draw_tree(4, 250)

wn.exitonclick()
