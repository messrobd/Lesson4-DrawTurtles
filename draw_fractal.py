import turtle
import math

window = turtle.Screen()
window.setup(width=500, height=500, startx=100, starty=100)
window.bgcolor("lightgrey")
pen = turtle.Turtle()

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

def calcTranslations(side):
    equilateral_internal_angle = 60#degrees
    angle = math.radians(equilateral_internal_angle)

    dx_1 = 0
    dy_1 = 0

    dx_2 = side
    dy_2 = 0

    dx_3 = -side / 2
    dy_3 = side * math.sin(angle)

    dx_translations = [dx_1, dx_2, dx_3]
    dy_translations = [dy_1, dy_2, dy_3]

    return dx_translations, dy_translations

def drawFractal(side, order, pen):
    pen.hideturtle()
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






#math.pow(3, order)






drawFractal(100, 2, pen)

window.exitonclick()

#tests
def tests():
    side = 100

    print calcDxDy(side)

#tests()
