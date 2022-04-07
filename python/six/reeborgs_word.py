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

# for n in range(0,6):
#     move()
#     jump()

while nb > 0:
    move()
    jump()
    nb -= 1
    print(nb)