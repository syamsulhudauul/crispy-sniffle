#hirst-painting
import colorgram
from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.hideturtle()
colormode(255)
# extract colors from image and save to list
colors = colorgram.extract('/Users/syamsulhudauul/py/18-gui-turtle/colorgram.png', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

# print(rgb_colors)

def draw_dot():
    tim.dot(20, random.choice(rgb_colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()

def draw_row():
    for _ in range(10):
        draw_dot()

# def draw_painting():
#     tim.penup()
#     tim.setpos(-250, -250)
#     tim.pendown()
#     for _ in range(10):
#         draw_row()
#         tim.penup()
#         tim.setpos(-250, tim.ycor()+50)
#         tim.pendown()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    draw_dot()
    if dot_count % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()

# draw_painting()
screen = Screen()
screen.exitonclick()