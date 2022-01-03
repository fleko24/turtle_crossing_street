from car import Car
import random

SHAPES = ['images/black_car.gif', 'images/blue_car.gif', 'images/green_car.gif', 'images/orange_car.gif',
          'images/pink_car.gif', 'images/purple_car.gif', 'images/red_car.gif', 'images/white_car.gif',
          'images/yellow_car.gif']

MOVE_INCREMENT = 2


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = 10

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Car(random.choice(SHAPES))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

