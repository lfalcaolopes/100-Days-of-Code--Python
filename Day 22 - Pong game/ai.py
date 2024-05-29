PADDLE_HEIGHT = 60
class Ai:
    def __init__(self):
        self.paddle = None

    def set_paddle(self, paddle):
        self.paddle = paddle

    def move(self, ball, command_queue):
        if ball.ball_direction < 90 or ball.ball_direction > 270:
            if ball.ycor() > self.paddle.ycor() + PADDLE_HEIGHT / 2:
                command_queue.put("UP")
            elif ball.ycor() < self.paddle.ycor() - PADDLE_HEIGHT / 2:
                command_queue.put("DOWN")
        else:
            if self.paddle.ycor() < 0:
                command_queue.put("UP")
            elif self.paddle.ycor() > 0:
                command_queue.put("DOWN")
