from turtle import Turtle
import random

INITIAL_X_POSITION = 420


class Car(Turtle):

    def __init__(self, shape):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shape(shape)
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.goto(INITIAL_X_POSITION, random.randint(-200, 190))






