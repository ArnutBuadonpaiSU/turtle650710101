"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

from turtle import *

speed(5)
bgcolor('black')
penup()
goto(-50,60)
pendown()
color('red')
begin_fill()
goto (100,100)
goto (100,-100)

#Draw windows
goto(-50,-60)
goto(-50,60)
end_fill()
color('black')
goto(15,73)

#cut 2 equal parts
color('white')
width(10)
goto (15,-75)
penup()
goto(95,0)
pendown()
goto(-45,0)

done()
    