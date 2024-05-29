from turtle import Turtle, Screen
from score import Scoreboard
from ball import Ball
from ai import Ai
import time

PADDLE_HEIGHT = 60
PADDLE_WIDTH = 10
class Field:
    def __init__(self):
        self.screen = Screen()
        self.scoreboard = Scoreboard()
        self.ball = Ball()
        self.ai = Ai()
        self.screen.tracer(0)
        self.screen.listen()

    def left_paddle(self):
        self.l_paddle = Turtle('square')
        self.l_paddle.color('white')
        self.l_paddle.up()
        self.l_paddle.setx(-350)
        self.l_paddle.setheading(90)
        self.l_paddle.shapesize(PADDLE_WIDTH / 20, PADDLE_HEIGHT / 20)

    def right_paddle(self):
        self.r_paddle = Turtle('square')
        self.r_paddle.color('white')
        self.r_paddle.up()
        self.r_paddle.setx(350)
        self.r_paddle.setheading(90)
        self.r_paddle.shapesize(PADDLE_WIDTH / 20, PADDLE_HEIGHT / 20)

    def field_divider(self):
        for i in range(10):
            self.divider = Turtle('square')
            self.divider.color('white')
            self.divider.up()
            self.divider.shapesize(1.5, 0.2)
            self.divider.sety(-270 + (60 * i))
    
    def l_up(self):
        if self.l_paddle.ycor() < 260:
            self.l_paddle.forward(30)

    def r_up(self):
        if self.r_paddle.ycor() < 260:
            self.r_paddle.forward(30)

    def l_down(self):
        if self.l_paddle.ycor() > -260:
            self.l_paddle.backward(30)

    def r_down(self):
        if self.r_paddle.ycor() > -260:
            self.r_paddle.backward(30)

    def setup(self):
        self.left_paddle()
        self.right_paddle()
        self.field_divider()
        self.scoreboard.left_score()
        self.scoreboard.right_score()
        self.ball.direction()
        self.ai.set_paddle(self.r_paddle)

        self.screen.update()

    def left_paddle_move(self):
        self.screen.onkey(self.l_up, 's')
        self.screen.onkey(self.l_down, 't')

    def right_paddle_move(self):
        self.screen.onkey(self.r_up, 'n')
        self.screen.onkey(self.r_down, 'e')

    def game_on(self):
        self.left_paddle_move()
        self.right_paddle_move()

        self.paddle_collision()
        self.ball.movement()

        self.goal_detector()

    def goal_detector(self):
        self.location = self.ball.ball_position()

        if self.location[0] > 360:
            self.ball.direction()
            self.ball.starter_ball()
            self.scoreboard.print_left_score()
            self.l_paddle.goto(-350, 0)
            self.r_paddle.goto(350, 0)
            time.sleep(1)
        elif self.location[0] < -360:
            self.ball.direction()
            self.ball.starter_ball()
            self.scoreboard.print_right_score()
            self.l_paddle.goto(-350, 0)
            self.r_paddle.goto(350, 0)
            time.sleep(1)

    def paddle_collision(self):
        position_ball = self.ball.ball_position()

        if position_ball[0] < -340 and self.ball.distance(self.l_paddle) <25:
            if self.ball.ball_direction == 135:
                self.ball.ball_direction = 45
            elif self.ball.ball_direction == 225:
                self.ball.ball_direction = 315
        elif position_ball[0] > 340 and self.ball.distance(self.r_paddle) < 25:
            if self.ball.ball_direction == 45:
                self.ball.ball_direction = 135
            elif self.ball.ball_direction == 315:
                self.ball.ball_direction = 225

    def distance_x_paddle_to_ball(self, paddle):
        return abs(self.ball.xcor() - paddle.xcor())

    def distance_y_paddle_to_ball(self, paddle):
        return abs(self.ball.ycor() - paddle.ycor())
        
    def calculate_new_angle(self, paddle):
        paddle_y = paddle.ycor()
        ball_y = self.ball.ycor()

        relative_y = ball_y - paddle_y

        new_angle = relative_y * 2

        if paddle == self.l_paddle:
            self.ball.ball_direction = (180 - new_angle) % 360
        else:
            self.ball.ball_direction = (360 - new_angle) % 360
            
    def ai_move(self, command_queue):
        self.ai.move(self.ball, command_queue)

    def process_commands(self, command_queue):
        while not command_queue.empty():
            command = command_queue.get()
            if command == "UP":
                self.r_up()
            elif command == "DOWN":
                self.r_down()
