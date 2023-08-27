from turtle import Turtle, Screen

timmie = Turtle()
# timmie.shape("turtle")
timmie.color("red")

# i = 0
# while i<4:
#     timmie.forward(100)
#     timmie.right(90)
#     i+=1


for _ in range(15):
    timmie.forward(10)
    timmie.penup()
    timmie.forward(10)
    timmie.pendown()

screen = Screen()
screen.exitonclick()