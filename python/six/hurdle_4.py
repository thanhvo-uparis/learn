def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()