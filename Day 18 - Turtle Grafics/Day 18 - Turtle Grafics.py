import turtle
from turtle import Turtle, Screen
import random

thommy = Turtle()
screen = Screen()

thommy.shape('turtle')
thommy.color('green')
turtle.colormode(255)

colors = ['grey', 'red', 'yellow', 'cyan', 'purple', 'blue', 'green']
angles = [0, 90, 180, 270]


def draw_shape(sides):
    for _ in range(sides):
        thommy.forward(100)
        thommy.right(360/sides)


def set_pos(x, y):
    thommy.up()
    thommy.goto(x, y)
    thommy.down()


def random_walk():
    thommy.hideturtle()
    while True:
        thommy.pencolor(random.choice(colors))
        thommy.forward(25)
        thommy.right(random.choice(angles))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    ran = (r, g, b)
    return ran


def spirograph():
    thommy.hideturtle()
    thommy.speed(0)

    for i in range(180):
        thommy.pencolor(random_color())
        thommy.circle(150)
        thommy.left(2)


def painting():
    def row():
        for dots in range(12):
            thommy.dot(25, random_color())
            thommy.forward(50)

    def r_column():
        thommy.left(90)
        thommy.forward(50)
        thommy.left(90)
        thommy.forward(50)

    def l_column():
        thommy.right(90)
        thommy.forward(50)
        thommy.right(90)
        thommy.forward(50)

    thommy.hideturtle()
    thommy.speed(0)
    set_pos(-300, -200)
    thommy.up()

    for rows in range(4):
        row()
        r_column()
        row()
        l_column()


def turt():
    def space(x):
        thommy.up()
        thommy.goto(x, 0)
        thommy.setheading(0)
        thommy.down()

    def t(x):
        thommy.up()
        thommy.forward(x/2)
        thommy.down()
        thommy.left(90)
        thommy.forward(x)
        thommy.left(90)
        thommy.forward(x/2)
        thommy.right(180)
        thommy.forward(x)

    def u(x):
        thommy.up()
        thommy.left(90)
        thommy.forward(x)
        thommy.down()
        thommy.right(180)
        thommy.forward(x)
        thommy.left(90)
        thommy.forward(x)
        thommy.left(90)
        thommy.forward(x)

    def r(x):
        thommy.left(90)
        thommy.forward(x)
        thommy.right(90)
        thommy.forward(x)
        thommy.right(90)
        thommy.forward(x/2)
        thommy.right(90)
        thommy.forward(x)
        thommy.left(153.435)
        thommy.forward(1.118*x)

    def moon():
        turtle.up()
        turtle.goto(240, -20)
        turtle.color('orange')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()

        turtle.up()
        turtle.goto(260, -20)
        turtle.color('dark blue')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()

    turtle.bgcolor('dark blue')
    thommy.width(5)

    space(-90)
    t(50)
    space(-30)
    u(50)
    space(30)
    r(50)
    space(90)
    t(50)

    thommy.up()
    thommy.goto(170, 10)
    thommy.setheading(20)

    moon()


screen.exitonclick()

