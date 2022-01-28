from turtle import Turtle, Screen
from food import Food
from score import Scoreboard
import time


class Snake:
    def __init__(self):
        self.segments = []
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.listen()
        self.head = Turtle()
        self.food = Food()
        self.scoreboard = Scoreboard()

    def setup(self):
        for i in range(3):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.up()
            new_segment.setx(-(20 * i))
            self.segments.append(new_segment)

        self.food.new_food()
        self.food_location = self.food.location()

        self.head = self.segments[0]
        self.screen.update()

    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)

    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)
        elif self.head.heading() == 270:
            self.head.left(90)

    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)

    def move(self):
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")

        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()

            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)
        self.screen.update()
        time.sleep(0.15)

    def size_up(self):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.up()

        last_x = self.segments[-1].xcor()
        last_y = self.segments[-1].ycor()

        new_segment.goto(last_x, last_y)
        self.segments.append(new_segment)

    def eating(self):
        self.food_location = self.food.location()

        food_x = self.food_location[0]
        food_y = self.food_location[1]

        head_x_location = round(self.head.xcor())
        head_y_location = round(self.head.ycor())

        if head_x_location == food_x and head_y_location == food_y:
            self.size_up()
            self.food.new_food()
            self.scoreboard.print_score()

    def is_hitting_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280:
            return True
        elif self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        else:
            return False

    def is_colliding(self):
        for segs in range(1, len(self.segments)):
            if self.head.distance(self.segments[segs]) < 15:
                return True

    def game_over(self):
        self.end = Turtle()
        self.end.up()
        self.end.color("white")
        self.end.speed(0)
        self.end.hideturtle()

        self.end.write(f"Game Over", False, 'center', ('Arial', 20, 'normal'))
