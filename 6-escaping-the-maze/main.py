# done the challenge on 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_left():
    print("turn left")

def at_goal():
    print("at goal")

def right_is_clear():
    print("right is clear")

def  move():
    print("move")

def front_is_clear():
    print("front is clear")

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def back():
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
            