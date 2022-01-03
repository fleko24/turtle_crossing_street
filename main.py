import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

GOAL_Y_POSITION = 240

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('images/background.gif')
screen.tracer(0)

# Player
tortuga = Player()

# Events
screen.listen()
screen.onkey(fun=tortuga.move_forward, key="Up")
screen.onkey(fun=tortuga.move_back, key="Down")

# cars
screen.addshape('images/black_car.gif')
screen.addshape('images/blue_car.gif')
screen.addshape('images/green_car.gif')
screen.addshape('images/orange_car.gif')
screen.addshape('images/pink_car.gif')
screen.addshape('images/purple_car.gif')
screen.addshape('images/red_car.gif')
screen.addshape('images/white_car.gif')
screen.addshape('images/yellow_car.gif')

# Scoreboard
scoreboard = Scoreboard()

is_game_on = True

car_manager = CarManager()

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision car
    for car in car_manager.cars:
        if car.distance(tortuga) < 30:
            is_game_on = False
            scoreboard.game_over()

    # Tortuga reach the goal
    if tortuga.ycor() >= GOAL_Y_POSITION:
        tortuga.back_to_initial_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
