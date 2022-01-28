from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.score = Turtle()
        self.score.up()
        self.score.color("white")
        self.score.speed(0)
        self.score.hideturtle()
        self.score.sety(270)
        self.points = 0
        self.high_score = 0
        self.score.write(f"Score: {self.points}", False, 'center', ('Arial', 20, 'normal'))

    def print_score(self):
        self.points += 1
        self.score.clear()
        self.score.write(f"Score: {self.points}", False, 'center', ('Arial', 20, 'normal'))
