from turtle import Turtle
import random

POSSIBLE_POSITION = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


class Food:
    def __init__(self):
        self.foods = []

    def new_food(self):
        new = Turtle("circle")
        new.color("blue")
        new.up()
        new.speed(0)
        new.shapesize(0.5, 0.5)

        rand_x = random.choice(POSSIBLE_POSITION)
        rand_y = random.choice(POSSIBLE_POSITION)
        new.goto(20 * rand_x, 20 * rand_y)

        self.foods.append(new)
        if len(self.foods) >= 2:
            self.foods[-2].hideturtle()
            if len(self.foods) >= 3:
                del self.foods[0]

    def location(self):
        place = [round(self.foods[-1].xcor()), round(self.foods[-1].ycor())]
        return place
