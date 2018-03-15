import turtle

window = turtle.Screen()
window.setup(width=500, height=500, startx=100, starty=100)
window.bgcolor("lightgrey")

def drawSolidTriangle(side, pen):
    #pen = turtle.Turtle()

    pen.fill(True)
    sides = 3
    while sides > 0:
        pen.forward(side)
        pen.left(120)
        sides -= 1
    pen.fill(False)

def drawFractal(side):
    pen = turtle.Turtle()

    left_turns = [0,0,120]
    forward_steps = [0,side,side]

    for turn, step in zip(left_turns, forward_steps):
        pen.left(turn)
        pen.forward(step)
        pen.right(turn)
        drawSolidTriangle(side, pen)














drawFractal(100)

window.exitonclick()
