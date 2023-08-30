import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# TODO 1: Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
player = Player()
screen.listen()
screen.onkey(player.move,"Up")

# TODO 2: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen.
car_manager = CarManager()
car_manager.create_car()

# TODO 5: Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase.
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    # TODO 4: Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars.
    car_manager.move_cars()

    # TODO 7: When the turtle collides with a car, GAME OVER should be displayed in the centre.
    # TODO 8: Detect when the turtle player collides with a car:
    if car_manager.check_collision(player):
        game_is_on = False
        # TODO 9: When the game is over, the turtle should appear back at the starting position.
        scoreboard.game_over()
        player.reset_position()
        
    # TODO 6: When the turtle hits the top edge of the screen, the turtle should move back to the starting position and the car speed should increase.
    if player.check_finish():
        car_manager.level_up()
        scoreboard.increase_level()
        player.reset_position()
        car_manager.reset_cars()

screen.exitonclick()