from turtle import Screen
from field import Field
import threading
import queue
import time

def start_ai_thread(field, command_queue):
    while True:
        field.ai_move(command_queue)
        time.sleep(0.135)

screen = Screen()
field = Field()

screen.bgcolor('black')
screen.setup(800, 600)

field.setup()

# Create a queue for AI commands
command_queue = queue.Queue()

# Start AI thread
ai_thread = threading.Thread(target=start_ai_thread, args=(field, command_queue))
ai_thread.daemon = True
ai_thread.start()

is_game_over = False

while not is_game_over:
    field.process_commands(command_queue)
    field.game_on()

screen.exitonclick()
