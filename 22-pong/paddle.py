from turtle import Turtle

STEP = 20

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(pos)

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()+STEP
        self.goto(x_cor,y_cor)

    def move_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()-STEP
        self.goto(x_cor,y_cor)
