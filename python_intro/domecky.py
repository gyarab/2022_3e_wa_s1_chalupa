from turtle import exitonclick, forward, right, left, back
from math import sqrt, asin, degrees
from random import randint


def house(width, height):
    diagonal = sqrt(height**2 + width**2)
    angle = degrees(asin(height / diagonal))

    # driveway
    forward(randint(10, 30))
    # walls
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    # diagonals
    left(angle)
    forward(diagonal)
    left(180 - angle)
    forward(width)
    left(90 + (90 - angle))
    forward(diagonal)
    left(angle)
    # roof
    left(90)
    forward(height)
    left(90 - angle)
    forward(diagonal / 2)
    left(2 * angle)
    forward(diagonal / 2)
    left(90 - angle)
    forward(height)
    left(90)
    forward(width)
    # driveway
    forward(randint(10, 20))


for i in range(randint(2, 10)):
    house(randint(50, 100), randint(50, 100))


exitonclick()
