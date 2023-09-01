from turtle import Turtle
# create a snake class
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake: 
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self,x,y):
        body = Turtle()
        body.penup()
        body.goto(x=x,y=y)
        body.color("white")
        body.shape("square")
        self.segments.append(body)

    def create_snake(self):
        # create a snake body
        for position in STARTING_POSITIONS:
            self.add_segment(x=position[0],y=position[1])

    def move(self):
        # make snake body follow the head
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # change snake direction up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        # change snake direction down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # change snake direction left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        # change snake direction left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def extend(self):
        # add a new segment to the snake
        self.add_segment(x=self.segments[-1].xcor(),y=self.segments[-1].ycor())

    def reset(self):
        # reset the snake
        for seg in self.segments:
            seg.color("black")
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
