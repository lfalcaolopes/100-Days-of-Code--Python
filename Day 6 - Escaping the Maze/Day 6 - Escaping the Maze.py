# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def face_north():
    while not is_facing_north():
        turn_left()

face_north()

while front_is_clear():
    move()
turn_left()
        
while not at_goal():
    if wall_on_right()==True:
       if wall_in_front()==True:
           turn_left()
       else:
           move()
    else:
        turn_right()
        move()