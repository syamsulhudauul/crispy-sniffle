from turtle import Turtle, Screen
import pandas

# Set up the screen
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

# set shape on screen
screen.addshape(image)

# add background image
turtle = Turtle()
turtle.shape(image)

# Read the data
data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Get the coordinates of the mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# Write the name of the state at the coordinates of the mouse click
def write_state_name(state):
    state_turtle = Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    x_coor = int(state.x)
    y_coor = int(state.y)
    loc = (x_coor, y_coor)
    state_turtle.goto(loc)
    state_turtle.write(state.state.item())

# Keep track of the correct guesses
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("./missing_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        print(state_data)
        write_state_name(state_data)

# Exit the screen
screen.exitonclick()