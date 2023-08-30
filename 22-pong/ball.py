from turtle import Turtle

STEP = 5

class Ball(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(pos)
        self.setheading(45)
        self.x_move = STEP
        self.y_move = STEP
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed += 0.01
    
    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()

