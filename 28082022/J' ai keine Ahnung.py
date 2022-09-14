Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.clear()
>>> for i in range (4):
	print (i)

	
0
1
2
3
>>> for i in range (4):
	turtle.forward(100)
	turtle.left (90)

	
>>> 
=========== RESTART: /home/pi/Documents/een vierkant schildpad.py ===========
>>> turte.clear()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    turte.clear()
NameError: name 'turte' is not defined
>>> turtle.clear()
>>> import turtle
>>> for i in range (6):
	turtle.forward(100)
	turtle.left(360/6)

	
>>> import turtle
>>> for i in range (8):
	turtle.forward(100)
	turtle.left(360/8)

	
>>> turtle.clear()
>>> import turtle
>>> turtle.color("green")
>>> turtle.pemsize(5)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    turtle.pemsize(5)
AttributeError: module 'turtle' has no attribute 'pemsize'
>>> turtle.pensize(5)
>>> turtle.bgcolor("black")
>>> for i in range (4):
	turtle.forward(100)
	turtle.left (90)
	for i in range (4):
	turtle.forward(100)



for i in range (4):
	turtle.forward(100)
	turtle.left (90)
	
	turtle.left (90)
	
SyntaxError: expected an indented block
>>> import turtle
>>> for i in range (4):
	turtle.forward(100)
	turtle.left(90)
	
