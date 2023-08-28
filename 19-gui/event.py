from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
    tim.forward(10)

# Higher order function
# passed move_forwards function as an argument to onkey() method
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

