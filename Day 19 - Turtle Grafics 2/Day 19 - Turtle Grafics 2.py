from turtle import Turtle, Screen
import random

screen = Screen()

colors = ['grey', 'red', 'yellow', 'cyan', 'purple', 'blue', 'green']


def etch_a_sketch():
    def front(x=5):
        thommy.forward(x)

    def back(x=5):
        thommy.backward(x)

    def clockwise(x=5, angle=5):
        thommy.right(angle)
        front(x)

    def counter_clockwise(x=5, angle=5):
        thommy.left(angle)
        front(x)

    thommy = Turtle()
    thommy.speed(0)

    screen.listen()
    screen.onkey(key="w", fun=front)
    screen.onkey(key="s", fun=back)
    screen.onkey(key="a", fun=counter_clockwise)
    screen.onkey(key="d", fun=clockwise)
    screen.onkey(key='c', fun=thommy.clear)


def turtle_racing():
    grey = Turtle()
    red = Turtle()
    yellow = Turtle()
    cyan = Turtle()
    purple = Turtle()
    blue = Turtle()
    green = Turtle()

    turtle = [grey, red, yellow, cyan, purple, blue, green]
    speed = [3, 5, 10]

    def turtle_setup():
        y_axis = -150
        counter = 0
        for turtles in turtle:
            turtles.shape('turtle')
            turtles.up()
            turtles.color(colors[counter])
            turtles.goto(-400, y_axis)

            y_axis += 50
            counter += 1

    def race():
        is_over = False
        counter = 0
        while not is_over:
            for turtles in turtle:
                turtles.forward(random.choice(speed))
                if turtles.xcor() >= 400:
                    is_over = True
                    break

        for turtles in turtle:
            if turtles.xcor() >= 400:
                winner = colors[counter]
            counter += 1

        if user_bet == winner:
            screen.textinput("And the winner is...", f"The {winner} turtle won! Congratulations.")
        else:
            screen.textinput("And the winner is...", f"The {winner} turtle won! Try again next time.")

    screen.setup(width=1200, height=500)
    screen.bgcolor('black')
    turtle_setup()

    user_bet = screen.textinput("Make a bet", "what turtle will win the race? Type a color: ")

    screen.listen()
    screen.onkey(key='space', fun=race)


turtle_racing()
screen.exitonclick()
