import turtle

window = turtle.Screen()
window.setup(width=500, height=500, startx=100, starty=100)
window.bgcolor("lightgrey")

def drawSolidTriangle(size):
    pen = turtle.Turtle()

    sides = 3
    while sides > 0:
        pen.forward(size)
        pen.left(120)
        sides -= 1














drawSolidTriangle(100)

window.exitonclick()
