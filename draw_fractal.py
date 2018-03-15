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

    drawSolidTriangle(side, pen)
    pen.forward(side)
    drawSolidTriangle(side, pen)













drawFractal(100)

window.exitonclick()
