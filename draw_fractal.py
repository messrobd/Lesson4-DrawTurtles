import turtle

window = turtle.Screen()
window.setup(width=500, height=500, startx=100, starty=100)
window.bgcolor("lightgrey")
pen = turtle.Turtle()
origin = -100, -100

pen.up()
pen.goto(origin)
pen.hideturtle()

def drawSolidTriangle(side, pen):
    #pen = turtle.Turtle()
    if not pen.isdown():
        pen.down()

    pen.fill(True)
    for _ in range (3):
        pen.forward(side)
        pen.left(120)
    pen.fill(False)
    pen.up()

def drawFractal(side, order, pen):
    pen.up()

    turns = [0, 0, 120]
    steps = [0, side, side]

    if order == 0:
        drawSolidTriangle(side, pen)
        return
    else:
        for turn, step in zip(turns, steps):
            pen.left(turn)
            pen.forward(step / 2)
            pen.right(turn)
            drawFractal(side / 2, order - 1, pen)
        #return pen to origin
        pen.right(120)
        pen.forward(side / 2)
        pen.left(120)

drawFractal(200, 3, pen)

window.exitonclick()
