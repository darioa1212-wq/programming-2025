# Draw complicated tree
# Dario Androsevic
# October 21st 2025
def draw_complicated_tree(level: int, branch_lenth: float):

    t.pendown()

    if level > 0:
        t.forward(branch_length)

        t.left(30)
        draw_complicated_tree(level - 1, branch_lenth * 0.6)

        t.right(20)
        draw_complicated_tree(level - 1, branch_lenth * 0.8)

        t.right(35)
        draw_complicated_tree(level - 1, branch_lenth * 0.9)

        t.left(25)
        t.backward(branch_length)

    else:
        t.color("green")
        t.stamp()
        t.color("brown")
