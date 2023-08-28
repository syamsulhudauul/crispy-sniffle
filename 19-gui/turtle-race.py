from turtle import Turtle, Screen
from random import randint

# turtle race project 

# create a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def is_valid_input(input):
    for color in colors:
        if input.lower() == color:
            return True
    return False

# create a screen object
screen = Screen()
screen.setup(width=500, height=400)
input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ")
while  not is_valid_input(input):
    input = screen.textinput(title="Invalid input", prompt="Reinput the color of turtle will win the race? ")

def get_step():
    return randint(0, 50)

# create a list of turtles
turtles = []
# looping through the colors list
for color in colors:
    # create a turtle object
    turtle = Turtle(shape="turtle")
    # set the color of the turtle
    turtle.color(color)
    # append the turtle object to the turtles list
    turtles.append(turtle)

# set the starting position of the turtles
y_position = -100

# looping through the turtles list
for turtle in turtles:
    # set the position of the turtle
    turtle.penup()
    turtle.goto(x=-230, y=y_position)
    # increase the y position
    y_position += 30

winner = ""

race_is_on = True
# start the race
while race_is_on:
    # looping through the turtles list
    for turtle in turtles:
        # move the turtle forward
        turtle.forward(get_step())
        if turtle.xcor() > 230:
            # exit the loop
            winner = turtle.pencolor()
            race_is_on = False
            break

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(x=-50,y=100)
# show screen text announce the winner
writer.pendown()
writer.write("=== Winner ===")

writer.penup()
writer.goto(x=-50,y=80)
writer.pendown()
writer.write(f"The winner is {winner} turtle")

writer.penup()
writer.goto(x=-50,y=60)
writer.pendown()
if winner == input:
    writer.write(f"You won!!!")
else:
    writer.write(f"You lose!!!")


screen.exitonclick()