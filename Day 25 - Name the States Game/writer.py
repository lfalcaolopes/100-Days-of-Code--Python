from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()

    def print_state(self, x, y, state):
        self.goto(x, y)
        self.write(state, False, 'center', ('Arial', 12, 'normal'))
