import turtle
turtle.speed(100)
turtle.pensize(7)
turtle.color("pink")
turtle.bgcolor("black")
turtle.begin_fill()
for i in range (100):
    turtle.forward(209)
    turtle.left(156)
turtle.end_fill()

turtle.up()
turtle.setposition(0, 100)
turtle.down()

turtle.color("LightBlue")
turtle.begin_fill()
for i in range (100):
    turtle.forward(209)
    turtle.left(156)
turtle.end_fill()

turtle.up()
turtle.setposition(-150,50)
turtle.down()

turtle.color("LightYellow")
turtle.begin_fill()
for i in range (100):
    turtle.forward(209)
    turtle.left(156)
turtle.end_fill()
