# Yang Liu
# CMPT 120 D400
# February 18, 2022

import turtle as t
import random

t.Screen().bgcolor("#caf9fa")

def draw_squares(color):
    t.penup()
    t.goto(100, 100)
    t.pendown()

    for i in range(4):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(50)
        t.left(90)

    t.penup()
    t.goto(-100, -100)
    t.pendown()

    for i in range(4):
        t.forward(50)
        t.left(90)
    
    t.end_fill()

def draw_circles(amt_circles):
    colors_list = ['red', 'green', 'blue']

    for i in range(amt_circles):
         t.penup()
         t.goto(random.randint(-200,200), random.randint(-200,200))
         t.pendown()
         t.fillcolor(random.choice(colors_list))
         t.begin_fill()
         t.circle(random.randint(10,40))
         t.end_fill()

def initials_and_studentno():
    # First name letter - Y
    t.penup()
    t.goto(200, -200)
    t.pendown()
    t.right(45)

    t.forward(45)
    t.left(90)
    t.forward(45)
    t.right(180)
    t.forward(45)
    t.left(45)
    t.forward(90)

    # Last name letter - L
    t.penup()
    t.goto(300, -200)
    t.pendown()

    t.forward(120)
    t.left(90)
    t.forward(45)

    # Student number digit - 9
    t.penup()
    t.goto(400, -250)
    t.pendown()
    t.circle(20)
    
    t.penup()
    t.goto(420, -230)
    t.pendown()

    t.right(90)
    t.forward(90)

    # Student number digit - 5
    t.penup()
    t.goto(450, -220)
    t.pendown()

    t.left(90)
    t.forward(45)
    t.left(180)
    t.forward(45)
    t.left(90)
    t.forward(45)

    t.left(90)
    t.forward(45)

    t.right(270)
    t.circle(30, -100)

    t.exitonclick()

draw_squares('purple')
draw_circles(5)
initials_and_studentno()
