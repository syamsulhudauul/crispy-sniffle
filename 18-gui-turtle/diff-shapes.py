from turtle import Turtle, Screen
import random

timmie = Turtle()
colours = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmie.forward(100)
        timmie.right(angle)

for shape_side_n in range(3, 11):
    timmie.color(random.choice(colours))
    draw_shape(shape_side_n)