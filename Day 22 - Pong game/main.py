from turtle import Screen
from field import Field

screen = Screen()
field = Field()

screen.bgcolor('black')
screen.setup(800, 600)

field.setup()

is_game_over = False

while not is_game_over:
    field.game_on()


screen.exitonclick()
