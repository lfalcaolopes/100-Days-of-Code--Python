import turtle
import pandas
from writer import Writer

screen = turtle.Screen()
writer = Writer()
screen.tracer(0)

image = "images/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("csv files/US_states.csv")

states_name = data.state
states_counter = 0
guessed_states = []

is_game_on = True

while is_game_on:
    screen.update()
    guess = turtle.textinput("Make your guess", "What state is missing?")

    if guess == "exit":
        is_game_on = False

    for states in states_name:
        if guess.lower() == states.lower():
            guessed_states.append(states)

            x_axis = int(data[data.state == guess.title()].x)
            y_axis = int(data[data.state == guess.title()].y)

            writer.print_state(x_axis, y_axis, states)

            screen.update()

            states_counter += 1

            if states_counter == 50:
                is_game_on = False

