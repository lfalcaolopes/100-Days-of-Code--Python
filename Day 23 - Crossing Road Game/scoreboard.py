from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 265)
        self.level = 1
        self.write(f"Level: {self.level}", False, 'center', ('Courier', 14, 'normal'))

    def print_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, 'center', ('Courier', 14, 'normal'))

    def game_over(self):
        self.end_game = Turtle()
        self.end_game.penup()
        self.end_game.hideturtle()
        self.end_game.write("GAME OVER", False, 'center', ('Courier', 30, 'normal'))