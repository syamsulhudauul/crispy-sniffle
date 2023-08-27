import random
from turtle import Turtle, Screen, colormode

timmie = Turtle()

timmie.pensize(10)
timmie.speed("fastest")
colormode(255)

#colours = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "black", "brown", "cyan", "magenta", "grey", "white"]

#random color in rgb
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color = (r,g,b)
    return random_color

# random walk 
# loop 100 times
# each time, randomly choose a direction and move forward 10 paces
# 0 = north, 90 = east, 180 = south, 270 = west
for _ in range(200):
    timmie.color(random_color())
    timmie.forward(20)
    timmie.setheading(random.choice([0,90,180,270]))
