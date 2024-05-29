from turtle import Turtle, Screen
import random
import time

DIRECTIONS = [45, 135, 225, 315]
BALL_SPEED = 2

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

        # keep square straight and not diagonal
        self.setheading(self.ball_direction + 45)
        self.forward(BALL_SPEED)
        self.setheading(self.ball_direction - 45)
        self.forward(BALL_SPEED)

        self.screen.update()
        time.sleep(0.01)

    def wall_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.ball_direction = self.reflect_angle(self.ball_direction)

    def reflect_angle(self, incident_angle):
        return 360 - incident_angle

    def ball_position(self):
        return [self.xcor(), self.ycor()]