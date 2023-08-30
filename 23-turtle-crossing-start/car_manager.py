from turtle import Turtle
from random import randint,choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance != 1:
            return
        
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.penup()
        new_car.color(choice(COLORS))
        new_car.goto(300,randint(-220,250))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def reset(self):
        self.car_speed = STARTING_MOVE_DISTANCE

    def reset_cars(self):
        for car in self.all_cars:
            car.goto(300,0)
            car.hideturtle()
        self.all_cars.clear()
    
    def level_up(self):
        self.reset_cars()
        self.increase_speed()
        self.create_car()
    
    # TODO 3: Detect when the turtle player collides with a car and stop the game if this happens.
    def check_collision(self,player):
        for car in self.all_cars:
            if car.distance(player)<20:
                return True
        return False

    def get_cars(self):
        return self.all_cars
    
    def get_speed(self):
        return self.car_speed