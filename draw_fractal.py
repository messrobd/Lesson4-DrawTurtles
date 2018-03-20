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

    turns = [0, 120, 240]
    steps = [side, side, side]

    if order == 0:
        drawSolidTriangle(side, pen)
        return
    else:
        #recursively call func in anticlockwise progression & return pen to origin 
        for turn, step in zip(turns, steps):
            drawFractal(side / 2, order - 1, pen)
            pen.left(turn)
            pen.forward(step / 2)
            pen.right(turn)

drawFractal(200, 3, pen)

window.exitonclick()
