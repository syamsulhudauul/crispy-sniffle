from turtle import Turtle, Screen, colormode
import random

# make spirograph
# 36 circles, each 10 degrees apart
# each circle is 100 long
# each circle is 5 degrees apart
# 360/36 = 10
# 360/5 = 72
# 72/2 = 36
# 36*10 = 360
# 36*5 = 180
# 180/2 = 90
# 90*10 = 900
# 90*5 = 450
# 450/2 = 225
# 225*10 = 2250
# 225*5 = 1125
# 1125/2 = 562.5
# 562.5*10 = 5625
# 562.5*5 = 2812.5
# 2812.5/2 = 1406.25

timmie = Turtle()
timmie.speed("fastest")
timmie.pensize(1)
colormode(255)

#random color in rgb
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color = (r,g,b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmie.color(random_color())
        timmie.circle(100)
        timmie.setheading(timmie.heading() + size_of_gap)
draw_spirograph(20)

screen = Screen()
screen.exitonclick()
