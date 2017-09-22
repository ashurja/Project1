# Jamshed Ashurov
# 09/19/2017
# flower.py
# This program creates a flower by using the hexagonal shapes

import turtle


def get_side_length():
    """
    This function asks the user to input the length of the side of the hexagons
    :return:
    """
    size = input("What is the side length of the hexagon?")
    return float(size)


def get_center_color():
    """
    This function asks the user to input the color of the central hexagon
    :return:
    """
    central_color = input("What is the color of the center?")
    return central_color


def center(size, color):
    """
    This function draws the central hexagon
    :param size:
    :param color:
    :return:
    """
    turtle.color(color)
    turtle.pencolor("black")
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(size)
        turtle.left(60)
    turtle.end_fill()


def get_petal_color():
    """
    This function asks the user to input the color of the outside hexagons
    :return:
    """
    petal_color = input("What is the color of the petals?")
    turtle.color(petal_color)
    return petal_color


def petals(size, color):
    """
    This function draws the outside hexagons
    :param size:
    :param color:
    :return:
    """
    turtle.color(color)
    turtle.pencolor("black")
    turtle.begin_fill()
    for x in range(6):
        turtle.forward(size)
        turtle.right(60)
    turtle.end_fill()
    for x in range(5):
        turtle.color(color)
        turtle.pencolor("black")
        turtle.begin_fill()
        turtle.right(120)
        for y in range(5):
            turtle.forward(size)
            turtle.right(60)
        turtle.end_fill()


def main():
    size = get_side_length()
    central_color = get_center_color()
    center(size, central_color)
    petal_color = get_petal_color()
    petals(size, petal_color)
    center(size, central_color)


main()


turtle.exitonclick()
