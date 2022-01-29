from turtle import Turtle, Screen
from score import Scoreboard
from ball import Ball
import time


class Field:
    def __init__(self):
        self.screen = Screen()
        self.scoreboard = Scoreboard()
        self.ball = Ball()
        self.screen.tracer(0)
        self.screen.listen()

    def left_paddle(self):
        self.l_paddle = Turtle('square')
        self.l_paddle.color('white')
        self.l_paddle.up()
        self.l_paddle.setx(-350)
        self.l_paddle.setheading(90)
        self.l_paddle.shapesize(1, 3)

    def right_paddle(self):
        self.r_paddle = Turtle('square')
        self.r_paddle.color('white')
        self.r_paddle.up()
        self.r_paddle.setx(350)
        self.r_paddle.setheading(90)
        self.r_paddle.shapesize(1, 3)

    def field_divider(self):
        for i in range(10):
            self.divider = Turtle('square')
            self.divider.color('white')
            self.divider.up()
            self.divider.shapesize(1.5, 0.2)
            self.divider.sety(-270 + (60 * i))

    def l_up(self):
        if self.l_paddle.ycor() < 260:
            self.l_paddle.forward(25)

    def r_up(self):
        if self.r_paddle.ycor() < 260:
            self.r_paddle.forward(25)

    def l_down(self):
        if self.l_paddle.ycor() > -260:
            self.l_paddle.backward(25)

    def r_down(self):
        if self.r_paddle.ycor() > -260:
            self.r_paddle.backward(25)

    def setup(self):
        self.left_paddle()
        self.right_paddle()
        self.field_divider()
        self.scoreboard.left_score()
        self.scoreboard.right_score()
        self.ball.direction()

        self.screen.update()

    def left_paddle_move(self):
        self.screen.onkey(self.l_up, 'w')
        self.screen.onkey(self.l_down, 's')

        self.screen.update()

    def right_paddle_move(self):
        self.screen.onkey(self.r_up, 'Up')
        self.screen.onkey(self.r_down, 'Down')

        self.screen.update()

    def game_on(self):
        self.left_paddle_move()
        self.right_paddle_move()

        self.paddle_collision()
        self.ball.movement()

        self.goal_detector()

    def goal_detector(self):
        self.location = self.ball.ball_position()

        if self.location[0] > 350:
            self.ball.direction()
            self.ball.starter_ball()
            self.scoreboard.print_left_score()
            time.sleep(1)
        elif self.location[0] < -350:
            self.ball.direction()
            self.ball.starter_ball()
            self.scoreboard.print_right_score()
            time.sleep(1)

    def paddle_collision(self):
        position_ball = self.ball.ball_position()

        if position_ball[0] < -330 and self.ball.distance(self.l_paddle) < 35:
            if self.ball.ball_direction == 270:
                self.ball.ball_direction = 0
            elif self.ball.ball_direction == 180:
                self.ball.ball_direction = 90
        elif position_ball[0] > 330 and self.ball.distance(self.r_paddle) < 35:
            if self.ball.ball_direction == 0:
                self.ball.ball_direction = 270
            elif self.ball.ball_direction == 90:
                self.ball.ball_direction = 180
