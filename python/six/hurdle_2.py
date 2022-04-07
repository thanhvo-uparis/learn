def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# test = False
# while test == False:
#     move()
#     jump()
#     if at_goal() == True:
#         test = True

while not at_goal():
    move()
    jump()

# or 

# while at_goal != True:
#     move()
#     jump()