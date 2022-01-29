from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.l_points = 0
        self.r_points = 0

    def left_score(self):
        self.l_score = Turtle()
        self.l_score.up()
        self.l_score.color("white")
        self.l_score.speed(0)
        self.l_score.hideturtle()
        self.l_score.goto(-50, 230)

        self.l_score.write(self.l_points, False, 'center', ('Arial', 40, 'normal'))

    def right_score(self):
        self.r_score = Turtle()
        self.r_score.up()
        self.r_score.color("white")
        self.r_score.speed(0)
        self.r_score.hideturtle()
        self.r_score.goto(50, 230)

        self.r_score.write(self.r_points, False, 'center', ('Arial', 40, 'normal'))

    def print_left_score(self):
        self.l_points += 1
        self.l_score.clear()
        self.l_score.write(self.l_points, False, 'center', ('Arial', 40, 'normal'))

    def print_right_score(self):
        self.r_points += 1
        self.r_score.clear()
        self.r_score.write(self.r_points, False, 'center', ('Arial', 40, 'normal'))
