from turtle import Turtle, Screen

SPEED = 15


class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.sety(-260)

    def up(self):
        self.forward(SPEED)

    def movement(self):
        self.screen.onkey(self.up, 'space')
        self.screen.update()

    def new_level(self):
        self.sety(-260)