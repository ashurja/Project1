# Jamshed Ashurov
# 09/06/2017
# Option 1.py
# This program makes four colored octagons

import turtle

# This function makes an octagon and changes the color of it


def makeanoctagon(color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(100)
        turtle.left(45)
    turtle.end_fill()


def movetheturtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


movetheturtle(0, 0)
makeanoctagon("blue")
movetheturtle(300, 0)
makeanoctagon("red")
movetheturtle(0, -300)
makeanoctagon("black")
movetheturtle(300, -300)
makeanoctagon("green")

turtle.exitonclick()
