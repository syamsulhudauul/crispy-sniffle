from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball((0,0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down,"Down")

screen.onkey(paddle2.move_up,"w")
screen.onkey(paddle2.move_down,"s")

def detect_collision_paddle(ball,paddle1,paddle2):
    # detect collision with wall
    # right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 and ball.xcor() < 340:
        ball.bounce_x()

    # left paddle
    if ball.distance(paddle2) < 50 and ball.xcor() < -320 and ball.xcor() > -340:
        ball.bounce_x()

def detect_collision_wall(ball):
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

game_is_on = True
while game_is_on: 
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    detect_collision_paddle(ball,paddle1,paddle2)
    detect_collision_wall(ball)

    # detect if ball goes out of bounds
    if ball.xcor() > 380:
        scoreboard.increase_score_l()
        ball.reset_position()
    if ball.xcor() < -380:
        scoreboard.increase_score_r()
        ball.reset_position()

screen.exitonclick()