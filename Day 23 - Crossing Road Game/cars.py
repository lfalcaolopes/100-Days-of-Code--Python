from turtle import Turtle, Screen
import random

SPEED = 5
INCREASE = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.colormode(255)
        self.random_color = (random.randint(0, 230), random.randint(0, 230), random.randint(0, 230))
        self.speed = SPEED
        self.car_list = []
        self.useful_cars = []
        self.level = 1
        self.penup()
        self.shape('square')
        self.shapesize(1, 2)
        self.setheading(180)
        self.goto(330, random.randint(-230, 230))
        self.color(self.random_color)

    def generate_car(self):
        if random.randint(1, 3) == 1:
            self.new_car = Cars()
            self.car_list.append(self.new_car)

    def move(self):
        for cars in self.car_list:
            cars.forward(self.speed)

    def level_up(self):
        self.speed += INCREASE

    def updated_car_list(self):
        for cars in self.car_list:
            if 50 > cars.xcor() > -50:
                self.useful_cars.append(cars)
        for u_cars in self.useful_cars:
            if u_cars.xcor() > 30 or u_cars.xcor() < -30:
                self.useful_cars.remove(u_cars)

