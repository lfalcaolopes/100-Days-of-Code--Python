from turtle import Screen, Turtle
from player import PlayerTurtle
from cars import Cars
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.listen()

turtle = PlayerTurtle()
car = Cars()
scoreboard = Scoreboard()

is_game_on = True
counter = 0

while is_game_on:
    car.updated_car_list()
    car.generate_car()
    turtle.movement()
    car.move()

    if turtle.ycor() > 270:
        scoreboard.print_score()
        car.level_up()
        turtle.new_level()

    for u_cars in car.useful_cars:
        if u_cars.distance(turtle) < 20:
            is_game_on = False



    screen.update()
    time.sleep(0.1)

scoreboard.game_over()

screen.exitonclick()
