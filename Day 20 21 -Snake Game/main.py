from turtle import Screen
from snake import Snake

screen = Screen()
snake = Snake()
screen.bgcolor("black")
screen.setup(width=600, height=600)

snake.setup()

is_game_over = False

while not is_game_over:
    snake.move()
    snake.eating()

    if snake.is_hitting_wall() or snake.is_colliding():
        is_game_over = True

snake.game_over()
screen.exitonclick()
