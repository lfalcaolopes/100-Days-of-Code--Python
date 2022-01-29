from turtle import Turtle, Screen
import random
import time

DIRECTIONS = [0, 90, 180, 270]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_direction = None
        self.shape('square')
        self.shapesize(0.5, 0.5)
        self.color('white')
        self.up()
        self.screen = Screen()

    def starter_ball(self):
        self.goto(0, 0)

    def direction(self):
        self.ball_direction = random.choice(DIRECTIONS)

    def movement(self):
        self.wall_collision()

        self.setheading(self.ball_direction)
        self.forward(5)
        self.setheading(self.ball_direction-90)
        self.forward(5)
        self.setheading(self.ball_direction)

        self.screen.update()
        time.sleep(0.01)

    def wall_collision(self):
        if self.ball_position()[1] > 280:
            if self.ball_direction == 90:
                self.ball_direction = 0
            elif self.ball_direction == 180:
                self.ball_direction = 270
        elif self.ball_position()[1] < -280:
            if self.ball_direction == 0:
                self.ball_direction = 90
            elif self.ball_direction == 270:
                self.ball_direction = 180

    def ball_position(self):
        return [self.xcor(), self.ycor()]