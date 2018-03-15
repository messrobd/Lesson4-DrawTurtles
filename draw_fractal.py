import turtle
import math

window = turtle.Screen()
window.setup(width=500, height=500, startx=100, starty=100)
window.bgcolor("lightgrey")

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

def drawFractal(side):
    pen = turtle.Turtle()
    pen.hideturtle()

    x_origin, y_origin = 0, 0
    dx_translations, dy_translations = calcTranslations(side)

    pen.up()
    pen.goto(x_origin, y_origin)
    for dx, dy in zip(dx_translations, dy_translations):
        x_pos = pen.xcor() + dx
        y_pos = pen.ycor() + dy
        pen.goto(x_pos, y_pos)
        drawSolidTriangle(side, pen)







#math.pow(3, order)






drawFractal(100)

window.exitonclick()

#tests
def tests():
    side = 100

    print calcDxDy(side)

#tests()
