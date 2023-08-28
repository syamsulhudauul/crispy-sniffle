from turtle import Turtle,Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor("black")

snake = Snake()

# important to trigger the listen() method here
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()

# create snake food 

# detect collision with food

# create a scoreboard

# detect collision with wall

# detect collision with tail
